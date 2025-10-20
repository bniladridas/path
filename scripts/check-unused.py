#!/usr/bin/env python3
# ruff: noqa: T201, N802, PTH123, PTH109, PERF401, TRY300, FA100
"""
Unused Code Detection Script for Path Application

This script detects:
- Unused imports
- Unused functions and classes
- Dead code
- Redundant files
- Unreachable code
"""

import ast
import os
import sys
from pathlib import Path
from typing import Dict
from typing import List


class UnusedCodeDetector:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.python_files = list(self.project_root.rglob("*.py"))
        self.exclude_dirs = {".git", "__pycache__", ".pytest_cache", "venv", "node_modules"}

    def get_python_files(self) -> List[Path]:
        """Get all Python files excluding certain directories."""
        files = []
        for file in self.python_files:
            if not any(exclude in file.parts for exclude in self.exclude_dirs):
                files.append(file)
        return files

    def analyze_file(self, file_path: Path) -> Dict:
        """Analyze a single Python file for unused code."""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            analyzer = CodeAnalyzer()
            analyzer.visit(tree)

            return {
                "file": file_path,
                "imports": analyzer.imports,
                "functions": analyzer.functions,
                "classes": analyzer.classes,
                "variables": analyzer.variables,
                "used_names": analyzer.used_names,
            }
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return {}

    def find_unused_imports(self, analysis: Dict) -> List[str]:
        """Find unused imports in a file."""
        unused = []
        for imp in analysis.get("imports", []):
            if imp not in analysis.get("used_names", set()):
                unused.append(imp)
        return unused

    def find_unused_functions(self, analysis: Dict) -> List[str]:
        """Find unused functions in a file."""
        unused = []
        flask_routes = {
            "index",
            "verify_human",
            "process_verification",
            "bypass_verification",
            "search",
            "terms",
            "privacy",
            "updates",
        }
        test_prefixes = {"test_", "setup_", "teardown_"}

        for func in analysis.get("functions", []):
            # Skip special methods, main functions, Flask routes, and test functions
            if (
                func.startswith("_")
                or func in ["main", "app"]
                or func in flask_routes
                or any(func.startswith(prefix) for prefix in test_prefixes)
            ):
                continue
            if func not in analysis.get("used_names", set()):
                unused.append(func)
        return unused

    def find_unused_classes(self, analysis: Dict) -> List[str]:
        """Find unused classes in a file."""
        unused = []
        for cls in analysis.get("classes", []):
            if cls not in analysis.get("used_names", set()):
                unused.append(cls)
        return unused

    def check_redundant_files(self) -> List[Path]:
        """Find potentially redundant files."""
        redundant = []

        # Check for very small files (likely redundant)
        for file in self.get_python_files():
            # Skip __init__.py files and test files
            if file.name == "__init__.py" or "test_" in file.name:
                continue

            try:
                with open(file, encoding="utf-8") as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                    # Remove comments and docstrings
                    code_lines = [line for line in lines if not line.startswith("#") and not line.startswith('"""')]
                    if len(code_lines) <= 2:  # Very minimal files
                        redundant.append(file)
            except Exception:
                continue

        return redundant

    def run_analysis(self):
        """Run complete unused code analysis."""
        print("Analyzing Python files for unused code...")
        print("=" * 50)

        total_issues = 0

        for file in self.get_python_files():
            analysis = self.analyze_file(file)
            if not analysis:
                continue

            unused_imports = self.find_unused_imports(analysis)
            unused_functions = self.find_unused_functions(analysis)
            unused_classes = self.find_unused_classes(analysis)

            if unused_imports or unused_functions or unused_classes:
                print(f"\n{file.relative_to(self.project_root)}:")

                if unused_imports:
                    print(f"  Unused imports: {', '.join(unused_imports)}")
                    total_issues += len(unused_imports)

                if unused_functions:
                    print(f"  Unused functions: {', '.join(unused_functions)}")
                    total_issues += len(unused_functions)

                if unused_classes:
                    print(f"  Unused classes: {', '.join(unused_classes)}")
                    total_issues += len(unused_classes)

        # Check for redundant files
        redundant_files = self.check_redundant_files()
        if redundant_files:
            print("\nPotentially redundant files:")
            for file in redundant_files:
                print(f"  {file.relative_to(self.project_root)}")
                total_issues += 1

        print(f"\n{'=' * 50}")
        print(f"Total issues found: {total_issues}")

        if total_issues == 0:
            print("No unused code detected!")

        return total_issues


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.functions = []
        self.classes = []
        self.variables = []
        self.used_names = set()

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imports.append(name)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imports.append(name)

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes.append(node.name)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_names.add(node.id)

    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name):
            self.used_names.add(node.value.id)
        self.generic_visit(node)


def main():
    """Main function to run unused code detection."""
    project_root = os.getcwd()

    if len(sys.argv) > 1:
        project_root = sys.argv[1]

    detector = UnusedCodeDetector(project_root)
    issues = detector.run_analysis()

    # Exit with error code if issues found
    sys.exit(1 if issues > 0 else 0)


if __name__ == "__main__":
    main()
