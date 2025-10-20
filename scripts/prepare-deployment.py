#!/usr/bin/env python3
"""
Deployment Preparation Script

This script prepares the project for different deployment targets:
- Vercel: Copies files to /path directory
- Docker: Ensures root files are up to date
- Local: Validates development setup

Usage:
    python scripts/prepare-deployment.py [target]

Targets:
    vercel  - Prepare for Vercel deployment
    docker  - Prepare for Docker deployment
    local   - Prepare for local development
    all     - Prepare for all targets (default)
"""

import shutil
import sys
from pathlib import Path


class DeploymentPrep:
    def __init__(self):
        self.root = Path.cwd()
        self.path_dir = self.root / "path"
        self.api_dir = self.root / "api"  # For Vercel deployment
        self.templates_dir = self.root / "templates"
        self.static_dir = self.root / "static"

    def print_status(self, message):
        print(f"[INFO] {message}")

    def print_warning(self, message):
        print(f"[WARN] {message}")

    def print_error(self, message):
        print(f"[ERROR] {message}")

    def ensure_path_structure(self):
        """Ensure PATH directory exists with required files."""
        self.path_dir.mkdir(exist_ok=True)

        # Check for required PATH files
        required_files = ["app.py", "index.py"]
        missing_files = []

        for file in required_files:
            if not (self.path_dir / file).exists():
                missing_files.append(file)

        if missing_files:
            self.print_error(f"Missing required PATH files: {', '.join(missing_files)}")
            return False

        return True

    def copy_templates(self):
        """Copy templates to PATH directory."""
        if not self.templates_dir.exists():
            self.print_error("Templates directory not found!")
            return False

        path_templates = self.path_dir / "templates"
        if path_templates.exists():
            shutil.rmtree(path_templates)

        shutil.copytree(self.templates_dir, path_templates)

        template_count = len(list(path_templates.glob("*.html")))
        self.print_status(f"Copied {template_count} template files to path/templates/")
        return True

    def copy_static_files(self):
        """Copy static files to PATH directory."""
        if not self.static_dir.exists():
            self.print_error("Static directory not found!")
            return False

        path_static = self.path_dir / "static"
        if path_static.exists():
            shutil.rmtree(path_static)

        shutil.copytree(self.static_dir, path_static)

        css_count = len(list(path_static.rglob("*.css")))
        self.print_status(f"Copied {css_count} CSS files to path/static/")
        return True

    def validate_structure(self):
        """Validate the deployment structure."""
        checks = [
            (self.templates_dir.exists(), "Root templates directory exists"),
            (self.static_dir.exists(), "Root static directory exists"),
            ((self.path_dir / "app.py").exists(), "PATH app.py exists"),
            ((self.path_dir / "index.py").exists(), "PATH index.py exists"),
        ]

        # Add Vercel-specific checks if api directory exists
        if self.api_dir.exists():
            checks.extend(
                [
                    ((self.api_dir / "templates").exists(), "API templates directory exists (Vercel)"),
                    ((self.api_dir / "static").exists(), "API static directory exists (Vercel)"),
                    ((self.api_dir / "app.py").exists(), "API app.py exists (Vercel)"),
                    ((self.api_dir / "index.py").exists(), "API index.py exists (Vercel)"),
                ]
            )

        all_passed = True
        for check, description in checks:
            if check:
                self.print_status(f"✓ {description}")
            else:
                self.print_error(f"✗ {description}")
                all_passed = False

        return all_passed

    def prepare_vercel(self):
        """Prepare for Vercel deployment."""
        self.print_status("Preparing for Vercel deployment...")

        # Create api directory for Vercel
        self.api_dir.mkdir(exist_ok=True)

        # Copy path files to api directory for Vercel
        for file in ["app.py", "index.py"]:
            src = self.path_dir / file
            dst = self.api_dir / file
            if src.exists():
                shutil.copy2(src, dst)
                self.print_status(f"Copied {file} to api/ directory")
            else:
                self.print_error(f"Missing required file: path/{file}")
                return False

        # Copy templates to api directory
        if self.templates_dir.exists():
            api_templates = self.api_dir / "templates"
            if api_templates.exists():
                shutil.rmtree(api_templates)
            shutil.copytree(self.templates_dir, api_templates)
            template_count = len(list(api_templates.glob("*.html")))
            self.print_status(f"Copied {template_count} template files to api/templates/")

        # Copy static files to api directory
        if self.static_dir.exists():
            api_static = self.api_dir / "static"
            if api_static.exists():
                shutil.rmtree(api_static)
            shutil.copytree(self.static_dir, api_static)
            css_count = len(list(api_static.rglob("*.css")))
            self.print_status(f"Copied {css_count} CSS files to api/static/")

        self.print_status("Vercel deployment preparation complete!")
        return True

    def prepare_docker(self):
        """Prepare for Docker deployment."""
        self.print_status("Preparing for Docker deployment...")

        # Docker uses root files, so just validate they exist
        if not self.templates_dir.exists():
            self.print_error("Templates directory missing for Docker deployment!")
            return False

        if not self.static_dir.exists():
            self.print_error("Static directory missing for Docker deployment!")
            return False

        if not Path("app_local.py").exists():
            self.print_error("app_local.py missing for Docker deployment!")
            return False

        self.print_status("Docker deployment preparation complete!")
        return True

    def prepare_local(self):
        """Prepare for local development."""
        self.print_status("Preparing for local development...")

        # Local development uses root files
        required_files = ["app_local.py", "requirements.txt"]
        missing_files = []

        for file in required_files:
            if not Path(file).exists():
                missing_files.append(file)

        if missing_files:
            self.print_error(f"Missing files for local development: {', '.join(missing_files)}")
            return False

        self.print_status("Local development preparation complete!")
        return True

    def prepare_all(self):
        """Prepare for all deployment targets."""
        self.print_status("Preparing for all deployment targets...")

        success = True
        success &= self.prepare_local()
        success &= self.prepare_docker()
        success &= self.prepare_vercel()

        if success:
            self.print_status("All deployment preparations complete!")
            return self.validate_structure()

        return False


def main():
    """Main function."""
    target = sys.argv[1] if len(sys.argv) > 1 else "all"

    prep = DeploymentPrep()

    if target == "vercel":
        success = prep.prepare_vercel()
    elif target == "docker":
        success = prep.prepare_docker()
    elif target == "local":
        success = prep.prepare_local()
    elif target == "all":
        success = prep.prepare_all()
    else:
        prep.print_error(f"Unknown target: {target}")
        prep.print_status("Available targets: vercel, docker, local, all")
        sys.exit(1)

    if success:
        prep.print_status(f"Deployment preparation for '{target}' completed successfully!")
        sys.exit(0)
    else:
        prep.print_error(f"Deployment preparation for '{target}' failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
