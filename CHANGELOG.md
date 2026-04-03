# 1.0.0 (2026-04-03)


### Bug Fixes

* align requirements.txt with pyproject.toml ([feb7f07](https://github.com/bniladridas/path/commit/feb7f07aeae6806e3fd136a0dae3b1b17a172955))
* allow conditional import ([2ec092c](https://github.com/bniladridas/path/commit/2ec092c92c0d5aeb46c7ca89153ce83a72cd3d97))
* api/index.py to import from path directory ([5caeb39](https://github.com/bniladridas/path/commit/5caeb3956df5649bdbca0040d60d61ec4a244ed6))
* back PYTHONPATH for imports ([cfca6ba](https://github.com/bniladridas/path/commit/cfca6ba4c01cec87049c85de280bc46c123b6918))
* build script for dependency installation ([1a8ba34](https://github.com/bniladridas/path/commit/1a8ba34d3255d64ec356e1f597b4265e1e060880))
* change app host to 127.0.0.1 for localhost access ([1673701](https://github.com/bniladridas/path/commit/1673701e86934157860ce473f5f37db18d6f3204))
* **ci:** apply Python 3.8 compatibility to all workflows ([4a22e75](https://github.com/bniladridas/path/commit/4a22e750fd78fd47ece5d0964ed348d249748646))
* **ci:** Docker build resilience and fallback options ([73e719e](https://github.com/bniladridas/path/commit/73e719e80324a8a9b6c9aea1a29f87d49f4b1a60))
* **ci:** improve Docker health check with better debugging ([a077e39](https://github.com/bniladridas/path/commit/a077e39b600970202409ac2fe3891c50938a572e))
* **ci:** prepare deployment files before running tests ([d06ff94](https://github.com/bniladridas/path/commit/d06ff94685a003db83f979d64f3f015c6ca0fb41))
* **ci:** replace non-existent GitHub actions ([eeb4d88](https://github.com/bniladridas/path/commit/eeb4d8895747a3d69967fa1218cbcd6bbc47febd))
* **ci:** simplify automated release workflow ([376b87a](https://github.com/bniladridas/path/commit/376b87a37b0573e0d6ab94a7a632d2511f72c653))
* **ci:** use valid node image tag ([927c02a](https://github.com/bniladridas/path/commit/927c02a42b9c585c8e536cda0b5712a0feb2e646))
* conditional webserver ([0a088c4](https://github.com/bniladridas/path/commit/0a088c4c7d500814d718916c933231185315e9e1))
* conditionally import dotenv for local dev ([e9563b3](https://github.com/bniladridas/path/commit/e9563b3dd788c2c82e16de119e12d57afc61b440))
* conditionally load dotenv for local dev only ([306e78a](https://github.com/bniladridas/path/commit/306e78af94832bc910ca2341b82fa5fdf6d881dd))
* correct FLASK_APP to module format for gunicorn ([5bc1148](https://github.com/bniladridas/path/commit/5bc1148f74148484b6140d5923408f43f43b3bae))
* correct PROJECT_ROOT for template paths ([f5892a3](https://github.com/bniladridas/path/commit/f5892a3ab4f1fa48f97d5a0f8e5551416965cc38))
* correct pylint workflow configuration ([085da8c](https://github.com/bniladridas/path/commit/085da8cae2e252b2bb026d52877f80fd3149d89e))
* correct vercel.json schema for build command ([59a17d7](https://github.com/bniladridas/path/commit/59a17d7aa731d9dbb2898ef9ee57caa3f8386d3d))
* current dir to path for app import ([84d9aa9](https://github.com/bniladridas/path/commit/84d9aa92249802d75062bf5cb9d9892eddc0855f))
* dependencies to pyproject.toml for Vercel ([9a71892](https://github.com/bniladridas/path/commit/9a71892f48e5abd6eb7c5e76ed0e32ecbd50c529))
* deps to pyproject.toml for Vercel ([17e850a](https://github.com/bniladridas/path/commit/17e850abb571812bd722942a8bc6efe6f705ddfa))
* **deps:** adjust Python support to 3.9+ for compatibility ([4ce78ce](https://github.com/bniladridas/path/commit/4ce78ce0a0eee7d4d92cdbf8ba35ccabf3e79ee8))
* **deps:** ensure Python 3.8 compatibility ([b2033ad](https://github.com/bniladridas/path/commit/b2033add30a69d9052794523d9e9df20d234c799))
* **deps:** resolve Flask-Werkzeug conflict for Python 3.8 ([8d1e3d5](https://github.com/bniladridas/path/commit/8d1e3d5aa009c856f334ea31d54b81ec25a26c1b))
* **deps:** standardize Python version to 3.10 across project ([ecd8fd1](https://github.com/bniladridas/path/commit/ecd8fd13cdda4c1290ad7767dcf2dd2ce63ab0cf))
* **deps:** update Python 3.8 requirements for compatibility ([a6137d3](https://github.com/bniladridas/path/commit/a6137d3dbd5143650d4ad8a7421d7a1008cb79cf))
* **deps:** update to stable package versions ([7881b7b](https://github.com/bniladridas/path/commit/7881b7b67e2856ec93801f705a14cc88e4619764))
* disable debug mode in test app for security ([6d588dc](https://github.com/bniladridas/path/commit/6d588dcfd7c84f0177ba8a5bc7a0b1aae0a39bff))
* **docker:** app.py entry point for Gunicorn ([6a0f7aa](https://github.com/bniladridas/path/commit/6a0f7aa152082eb1da7569185b78a2304b36a709))
* explicit python runtime config ([5ccfc82](https://github.com/bniladridas/path/commit/5ccfc822fa8d061187dcfe145e439e7cd7c76dc0))
* flask-openapi3 to py38 requirements ([beb31ac](https://github.com/bniladridas/path/commit/beb31acca6d60909b249f24fdff44bf66bd56c9c))
* follow redirects in env vars test ([eada0ff](https://github.com/bniladridas/path/commit/eada0ffbfedbfcfdce64a0c6aca35054a891049c))
* format code with ruff ([b4cc9e3](https://github.com/bniladridas/path/commit/b4cc9e318518317380707a9b77515b78af5689f6))
* format YAML files and fix linting issues ([a06f2e6](https://github.com/bniladridas/path/commit/a06f2e6d0b9d1bbcbf092a96ab47b13dd3b42b05))
* graceful rate limit handling ([ebc479e](https://github.com/bniladridas/path/commit/ebc479ea88ae9751be7e26b705562238c4c1cbad))
* human verification keywords ([bcf5414](https://github.com/bniladridas/path/commit/bcf541424a094ebf082b070dde7ab96d12d7b909))
* image generation submit handler ([7fea6de](https://github.com/bniladridas/path/commit/7fea6defc3bf10424914699f729bf219f2c9adba))
* implement custom vercel build script ([1d16d4c](https://github.com/bniladridas/path/commit/1d16d4c26b3fc3de4b4b7cbb986cff7d09e949b0))
* improve e2e test reliability and ci setup ([#44](https://github.com/bniladridas/path/issues/44)) ([8373644](https://github.com/bniladridas/path/commit/837364491ccfb046cd1a957be188ee03b4874c12))
* improve pylint workflow formatting ([79f80fa](https://github.com/bniladridas/path/commit/79f80fabb963782fd44805c8b5f1062124ae42fe))
* improve route tests and fix yaml linting ([b435592](https://github.com/bniladridas/path/commit/b435592a515004a3e2f78c30654fb56743c3253d))
* issues permission for semantic-release ([8ada78e](https://github.com/bniladridas/path/commit/8ada78edf96e847ba78db56c241f8bec9fcd048a))
* let Vercel auto-detect Python version ([43310f4](https://github.com/bniladridas/path/commit/43310f4f705dff71239cdd31d1a3d78bc5a70411))
* **lint:** per-file ignore for AST visitor methods ([a912383](https://github.com/bniladridas/path/commit/a9123838d539d6784a2ea525e5cf71c174330f19))
* **lint:** resolve ruff warnings and config deprecations ([1ac26b3](https://github.com/bniladridas/path/commit/1ac26b373bf93a63d67753cb1b918fa714b41a78))
* make dotenv import optional for deployment ([84a17db](https://github.com/bniladridas/path/commit/84a17dbe9eb962ce371847d9e3cf7caa6723800f))
* make google-generativeai import optional for Vercel ([f9bb468](https://github.com/bniladridas/path/commit/f9bb468944560629b2ba36a2819134f3cb6acb08))
* make imports more robust for Vercel deployment ([5c713de](https://github.com/bniladridas/path/commit/5c713dea43cbeb000ebca5301c09ecd59386b1fe))
* missing dependencies to api requirements ([6b080d9](https://github.com/bniladridas/path/commit/6b080d92ea2ae9faa7102165301e469a99bd7216))
* missing packages to path/requirements.txt ([306e373](https://github.com/bniladridas/path/commit/306e3734948d52e1912d95dad27eacaa3f29336b))
* move app and assets to api dir for vercel ([d235e07](https://github.com/bniladridas/path/commit/d235e0707d9b0d01d5cb2bb441264c1028bae082))
* move app.py to root for Vercel deployment ([4908411](https://github.com/bniladridas/path/commit/490841129f9ae7730b8d810701ecea7fae73cf46))
* move import inside function ([80d389d](https://github.com/bniladridas/path/commit/80d389da1bda6fea723145c060e4c3767477daf1))
* move includefiles inside config in vercel.json ([f688185](https://github.com/bniladridas/path/commit/f6881858c0e77bb189f6b0eb80442c9445aaca1b))
* nosec comments for bandit security warnings ([f3b2752](https://github.com/bniladridas/path/commit/f3b27520f711d4a06d27ba4deb3366f0082bd872))
* pip install command to vercel config ([0a81501](https://github.com/bniladridas/path/commit/0a81501b2b7515e237a82dcfb87a01c59a090c76))
* prevent pytest from collecting app routes as tests ([d091ddb](https://github.com/bniladridas/path/commit/d091ddb601a00b91c83469e3316ded2b2581f9f8))
* Python runtime config to vercel.json ([ed0da6c](https://github.com/bniladridas/path/commit/ed0da6c1328eada33d82308c22486b112364acad))
* Python runtime version to Vercel config ([ee092ca](https://github.com/bniladridas/path/commit/ee092cab0b2efaf58fbd3978ddd474ffdf0ed99a))
* rebase before push in auto-release ([1d529eb](https://github.com/bniladridas/path/commit/1d529eb412a939ef5cbe138391efd63d3181dd22))
* remove api dir and use path for Vercel functions ([69e22fc](https://github.com/bniladridas/path/commit/69e22fcc3a759aa4a30582dff14b66c47002e187))
* remove api directory and use legacy Vercel config ([2b216b9](https://github.com/bniladridas/path/commit/2b216b9f6a632968899f13de46b4b6d76cb3fd9b))
* remove api key ([f01cde5](https://github.com/bniladridas/path/commit/f01cde5b7b5ddf70a0e20c27b702bdeceb78cf37))
* remove custom install command to fix vercel deps ([e63014e](https://github.com/bniladridas/path/commit/e63014e4677c241cbf622156c9f459c271c3e093))
* remove dotenv dependency for deployment ([f72cd53](https://github.com/bniladridas/path/commit/f72cd5374426fc0d76154244fbd6e764d9c52f49))
* remove duplicate requirements.txt from path ([5a81f58](https://github.com/bniladridas/path/commit/5a81f58ec6f2ed508a631a662ab965bb15349500))
* remove extra whitespace in vercel.json ([98e1eda](https://github.com/bniladridas/path/commit/98e1edaa909c8128ceddb2a9679b6a2cefd800be))
* remove invalid -e from requirements-vercel.txt ([75eb25b](https://github.com/bniladridas/path/commit/75eb25bdbf52709bfb5c9140c78e6e8eb0354935))
* remove invalid installcommand from vercel.json ([99dcc76](https://github.com/bniladridas/path/commit/99dcc76b156cc5b49d56ad3090c9bc797b325f09))
* remove invalid runtime config ([6c77669](https://github.com/bniladridas/path/commit/6c77669d86ab0c46805f7b07fda59c5115e98b53))
* remove PYTHONPATH from vercel config ([49eee0c](https://github.com/bniladridas/path/commit/49eee0c4aee6d6575116996c3c7583daad904a5b))
* remove PYTHONPATH from vercel.json ([224b82c](https://github.com/bniladridas/path/commit/224b82c212d8fa40b4304c61ff231f06f038ff3e))
* remove unused import and dotenv loading ([05d6465](https://github.com/bniladridas/path/commit/05d6465eb9de0577f59ecc315ab7be5c75c6254a))
* rename root app.py to avoid import conflict ([b34255e](https://github.com/bniladridas/path/commit/b34255ef3168b240b2896a1dbfff0a89455773c2))
* requests import order and flask_openapi3 imports ([25c4f5c](https://github.com/bniladridas/path/commit/25c4f5cc5701c02662e221d36855f5c1cac022ee))
* restore previous changes and update documentation ([5de3137](https://github.com/bniladridas/path/commit/5de3137e14f4a8ecd843edcc8f45a62b1c8e30ed))
* restore table borders and bg ([ac2f025](https://github.com/bniladridas/path/commit/ac2f025e1397c8ec13aacb2096471abada8d404c))
* reuse server in playwright ([80858d7](https://github.com/bniladridas/path/commit/80858d75df54542f922dca074377e7f94b44b02e))
* revert vercel.json to include builds for deployment ([60df4a4](https://github.com/bniladridas/path/commit/60df4a48edb7a79472af788c78454e809da7974a))
* revert vercel.json to working config ([5c41dde](https://github.com/bniladridas/path/commit/5c41dde5d404703900c131a322478e28ec48b7d8))
* sanitize query in logs to prevent log injection ([51e0f28](https://github.com/bniladridas/path/commit/51e0f2816d148e7e5f61d8aae7172cf462bfcd1c))
* sanitize user input before logging ([fe5d47d](https://github.com/bniladridas/path/commit/fe5d47d4811a5fc3623c22f59fd8e783e7568b35))
* **security:** configure Bandit for web app patterns ([5b8581c](https://github.com/bniladridas/path/commit/5b8581ccb3cd26b96af0df78d23af65f0d78a2f6))
* **security:** correct Bandit config file format ([50e52e4](https://github.com/bniladridas/path/commit/50e52e4c0918a202e67e1a48f745b25fc1f49ef7))
* **security:** resolve Bandit B112 warning ([6f42e1b](https://github.com/bniladridas/path/commit/6f42e1bfbcd0d5322e5ff3c0dbff0119fcb47878))
* **security:** resolve Jinja2 vulnerabilities and pin deps ([24e57b9](https://github.com/bniladridas/path/commit/24e57b990ae373e0e3ab925cedb897d04eeee4cb))
* set template and static folders to project root paths ([37026e2](https://github.com/bniladridas/path/commit/37026e247c4e614422e1454a3f9fb77102220996))
* simplify api/index.py import structure ([bdd3a34](https://github.com/bniladridas/path/commit/bdd3a342fb6f6c52a19effea096971cddce901b8))
* simplify Flask app for Vercel compatibility ([0fec6c0](https://github.com/bniladridas/path/commit/0fec6c04cf9f61d47abd134968352b111884a570))
* simplify vercel configuration ([28750f3](https://github.com/bniladridas/path/commit/28750f3a1a89abe7ed3f1f2430f50e33ee446f3a))
* specify python3.12 runtime for Vercel ([653612b](https://github.com/bniladridas/path/commit/653612bcc01fedf35b14ac496466cc6e131df5f2))
* specify requirements path in vercel config ([c6a36a9](https://github.com/bniladridas/path/commit/c6a36a90cf019993dd89d6c7015b324bd244ebb3))
* suppress DeprecationWarnings in pytest ([9c936d7](https://github.com/bniladridas/path/commit/9c936d75d729071375217cca0efcc0724af47998))
* switch to modern Vercel functions format ([e126e87](https://github.com/bniladridas/path/commit/e126e875782ea2a92c3879c882524ba1852dff6f))
* ternary expressions in check-unused ([c7dbbf9](https://github.com/bniladridas/path/commit/c7dbbf9188301a80a3f5c95c6f506f7847f2f5f0))
* **tests:** update imports from api to path module ([12385b8](https://github.com/bniladridas/path/commit/12385b80decedfe0c12a33a4fa42fc4278307c88))
* trailing whitespace ([8847906](https://github.com/bniladridas/path/commit/8847906cc456e35240d1359a8b13adf71acefd44))
* update build configuration and dependencies ([dd79e3c](https://github.com/bniladridas/path/commit/dd79e3c3021916c5e5dfea6506a58ea966b9fa58))
* update build process for dependency installation ([4a7973b](https://github.com/bniladridas/path/commit/4a7973bb99e4227b73372b02b16929e619de1e6d))
* update config ([45ac4da](https://github.com/bniladridas/path/commit/45ac4da1d0d399c5bdbcfc21e0193baeac4783d8))
* update config ([da81827](https://github.com/bniladridas/path/commit/da81827cf64215251437f319e2b0037ba025e83d))
* update Dockerfile to use app_local.py ([5aef7a8](https://github.com/bniladridas/path/commit/5aef7a8709c0599cd904fe0d2a2f965faa11c779))
* update e2e workflow for path/app.py ([042a264](https://github.com/bniladridas/path/commit/042a264c0e874539ade4f6e7ef1f013c9959da00))
* update gunicorn CMD to path.app:app ([7083b12](https://github.com/bniladridas/path/commit/7083b129c3ce5be788a153e818d9e5799264f409))
* update itsdangerous for flask 3.1.2 compatibility ([e96ba59](https://github.com/bniladridas/path/commit/e96ba591f548769a240382cc440d39c9e6b0e5c8))
* update Jinja2 to fix security vulnerabilities ([92b3aa5](https://github.com/bniladridas/path/commit/92b3aa50b60d169c9ecf8bc574e4921836b2fa4c))
* update port from 5000 to 8000 ([2c8f31c](https://github.com/bniladridas/path/commit/2c8f31c62211a79b5587888adaad48204b520a5a))
* update python-dotenv for Python 3.8-3.12 compatibility ([76d759b](https://github.com/bniladridas/path/commit/76d759b1669ce0fa75cb74e4c33a4aedc2094db2))
* update python-dotenv version ([a1527e2](https://github.com/bniladridas/path/commit/a1527e2f9efd976e273c75d854161d04b6796152))
* update readme links and formatting ([0ac5e74](https://github.com/bniladridas/path/commit/0ac5e74e445d2d0796970808b61487f31863e04e))
* update references to app.py in scripts and configs ([deec3ec](https://github.com/bniladridas/path/commit/deec3ecf04aa7c28c78b5dfd48be849768af79f9))
* update requests implementation for vercel ([b81b26e](https://github.com/bniladridas/path/commit/b81b26ec8ca8dd9afda79c3b5d4dda098b98189b))
* update requests to 2.32.4 (2.32.5 doesn't exist) ([305a6f1](https://github.com/bniladridas/path/commit/305a6f10c07e559fe040c6c06568a3143ce85a4f))
* update requirements and vercel config for deployment ([3aa3e5d](https://github.com/bniladridas/path/commit/3aa3e5db6d9f28bceddcdb91ff14ab5d5069a3ae))
* update root requirements.txt to match path versions ([1e34ffa](https://github.com/bniladridas/path/commit/1e34ffa103e55c5dd3b1eba3bc0b634078d89a76))
* update scripts for app.py in root and path/ structure ([9e70fb5](https://github.com/bniladridas/path/commit/9e70fb5f0780f006d511abd44cbff745e9428d7f))
* update template/static paths after moving app.py ([f29b371](https://github.com/bniladridas/path/commit/f29b371aa57b2b7c1b271ade73a53156368aa690))
* update test imports and app name check ([65db25a](https://github.com/bniladridas/path/commit/65db25aea43cc77f44481cfeb2b2fb65f3350a9a))
* update uv lockfile ([2a0e2e7](https://github.com/bniladridas/path/commit/2a0e2e73e09efed695b0b00885c69aa607dabb08))
* update vercel config and python runtime ([947e3ed](https://github.com/bniladridas/path/commit/947e3ed73acdad7366e043935b89ae2291d50d89))
* update Vercel config for api directory ([d8db33a](https://github.com/bniladridas/path/commit/d8db33af16cf093fa9268044b6946a20a36e8dfc))
* update vercel config for better python support ([fb9b0b3](https://github.com/bniladridas/path/commit/fb9b0b3cc503f2df3fc69deb56528137934865d1))
* update Vercel config for nested path structure ([6b8dbf0](https://github.com/bniladridas/path/commit/6b8dbf08b450e7b27895e62b47e1062bd6bb342d))
* update vercel config for python 3.11 ([fb3fd49](https://github.com/bniladridas/path/commit/fb3fd491fc653bb66bd461310d08dbb614b27b3e))
* update vercel config with explicit python 3.9 runtime ([a53ffd1](https://github.com/bniladridas/path/commit/a53ffd19f592704aee308383b8cda52e160613f0))
* update vercel configuration for python dependencies ([3c43f2e](https://github.com/bniladridas/path/commit/3c43f2eeeceb96b8a81557dfafc241a66363e504))
* update vercel package to version 0.3.2 ([50363b7](https://github.com/bniladridas/path/commit/50363b7bc24f3f5272e5befc5af7ebaffa1ce015))
* update vercel runtime to 3.9+ for compatibility ([4759d53](https://github.com/bniladridas/path/commit/4759d5398d45607401483a02ea8865166ee567c1))
* update vercel runtime to 3.9+ for compatibility ([ca0670e](https://github.com/bniladridas/path/commit/ca0670e9555a8dd177255633fda56402d87c6590))
* update vercel validation workflow for path/app.py ([4496f6a](https://github.com/bniladridas/path/commit/4496f6a664347c80043dd497e71c14594b475362))
* update vercel.json with correct runtime configuration ([74e8732](https://github.com/bniladridas/path/commit/74e8732bb70061045689484cbe934d0a391821d4))
* update werkzeug and vercel versions for compatibility ([cd1064e](https://github.com/bniladridas/path/commit/cd1064e619acadef3e78c061b2054a24946ad99c))
* update workflow for app.py in root ([e13038f](https://github.com/bniladridas/path/commit/e13038fcf7c9724b363fde34c42cad1784b257f0))
* use @vercel/python@5.7.1 ([ce4f59f](https://github.com/bniladridas/path/commit/ce4f59fe6b322d97a3f2ae1d1717b7942d805fb6))
* use css vars and thead/tbody ([97a992f](https://github.com/bniladridas/path/commit/97a992fb61d938f7f729ffe7ef475ba0274f6322))
* use default Python runtime for Vercel ([490d35c](https://github.com/bniladridas/path/commit/490d35c4031e4a91a44163bc75e840d08d973dfe))
* use macos-14 runner ([4e3811a](https://github.com/bniladridas/path/commit/4e3811a87b1ad1b99a224f6a3c2976323dd05932))
* use modern vercel config with rewrites ([db162df](https://github.com/bniladridas/path/commit/db162df134bf16f07f28df4b18d1945b389ffd85))
* use py38 requirements in vercel build simulation ([46de3e8](https://github.com/bniladridas/path/commit/46de3e81dbfc76daf34f4186dfedc0e999d7ef44))
* use py38 requirements in vercel build simulation ([c02a764](https://github.com/bniladridas/path/commit/c02a7640d013787fa2d9c50c153eadd7d507c483))
* use py38 requirements in vercel validation for 3.8 ([59531a0](https://github.com/bniladridas/path/commit/59531a02ffe3f1d364b81da795eb517bba860ef4))
* use python3.10 runtime for Vercel ([e295fa1](https://github.com/bniladridas/path/commit/e295fa1201cae3fb86a2f0654d760f616f8705d2))
* use python3.11 runtime ([77eebc3](https://github.com/bniladridas/path/commit/77eebc3a73c2655254130bfeb8558139deb4bcf2))
* use python3.11 runtime for Vercel compatibility ([97c7ff9](https://github.com/bniladridas/path/commit/97c7ff9a920ecfbc911b1d21992272da0a619b6f))
* use python3.9 runtime for Vercel ([071149b](https://github.com/bniladridas/path/commit/071149b5996854d1cf9fb82530ba72db0dd6bdda))
* use root requirements.txt for Vercel ([5026acc](https://github.com/bniladridas/path/commit/5026acc2cbf4fd5a0ff6563959c8e371449ad6ad))
* use valid Python runtime version for Vercel ([a03512f](https://github.com/bniladridas/path/commit/a03512fc579858383702da0cdecc738e9dc2a7d7))
* **vercel:** resolve 404 error after api to path rename ([15115ce](https://github.com/bniladridas/path/commit/15115ced37ac2a3b3aafe453965e0bcb14e47607))
* **vercel:** resolve conflicting functions and builds config ([57c4c2d](https://github.com/bniladridas/path/commit/57c4c2dcbbc6e5cf8a3068bbaaee6ff5f8fd4fd5))
* **vercel:** specify Python runtime version ([9b18563](https://github.com/bniladridas/path/commit/9b18563982a6ceda55a2152db2dd17ff932a7c6d))


### Features

* /status endpoint for API health checks ([4757868](https://github.com/bniladridas/path/commit/47578686294d19f0da006f4b8c27c1aecc88c6e1))
* allow users to their own gemini api key ([775a83f](https://github.com/bniladridas/path/commit/775a83f3393e1e7ca7af00b4d5da505f12af524f))
* **ci:** Python 3.8-3.12 matrix testing ([a998559](https://github.com/bniladridas/path/commit/a99855954262765b050856c00dbc6f5372d2ecdd))
* **ci:** restore Python 3.8 support with compatibility ([9c2a829](https://github.com/bniladridas/path/commit/9c2a8293a9b7907fcf398c2662b7683c769b0b12))
* colored ANSI logging to all workflow steps ([0d1af3b](https://github.com/bniladridas/path/commit/0d1af3b8a76e80e53452961c6476fa47c9a8d638))
* colored ANSI logging to e2e.yml workflow ([2d9cdbf](https://github.com/bniladridas/path/commit/2d9cdbf000186a0e25e20340b2715e37b22c0c6e))
* comprehensive unused code detection tools ([897c501](https://github.com/bniladridas/path/commit/897c50165c6fc039a7a4851d414fc6cf36e5022d))
* conventional commit standards and scripts ([6ee5ee9](https://github.com/bniladridas/path/commit/6ee5ee94f847478db38a7d3fc0dc31a9347a90e4))
* conventional commit standards and scripts ([a23797a](https://github.com/bniladridas/path/commit/a23797a8ebfe63b247582daff1f26f4321133212))
* **docker:** dual registry support (GHCR + Docker Hub) ([5e9a07a](https://github.com/bniladridas/path/commit/5e9a07ae4aa54c8679bf872c4b61f25d1897eef0))
* enhance OpenAPI spec with models and tags ([8cc904f](https://github.com/bniladridas/path/commit/8cc904f3eb86b21f0899f8a339e9560b17f7efd9))
* fully automated release system ([4f83f7a](https://github.com/bniladridas/path/commit/4f83f7ab67c6733f2120b58c88bd355f4bd7ecda))
* google-generativeai for AI features ([8d9919d](https://github.com/bniladridas/path/commit/8d9919d130fd22f8d36de89d8edffce5aa1ba73d))
* load api key from ~/.harper.env ([258d923](https://github.com/bniladridas/path/commit/258d9237b12a28580ed110af6133a8af970aab57))
* logging for Vercel debugging ([efd0d44](https://github.com/bniladridas/path/commit/efd0d448efe55f97505b2447bbb914ede9a914f0))
* OpenAPI spec, versioning, status endpoint ([8c9da86](https://github.com/bniladridas/path/commit/8c9da866dd2c05ee9d754f3fe1ebdfc36d434864))
* print() with noqa for Vercel logging ([df04839](https://github.com/bniladridas/path/commit/df048394cb46ca914604068680e90d93ba301d59))
* Python 3.9 support with legacy google-generativeai ([#105](https://github.com/bniladridas/path/issues/105)) ([9701841](https://github.com/bniladridas/path/commit/970184190dcb6605e245d5b69318f3676a5bfcca))
* replace emojis with ANSI colored logging ([80e6364](https://github.com/bniladridas/path/commit/80e6364b3c5acddfad69265e45e52bd58d7bb64e))
* rust native binary cli ([e851050](https://github.com/bniladridas/path/commit/e851050c4c3751c03350962ae671d8a596f93bf0))
* static file routing for Vercel deployment ([515959f](https://github.com/bniladridas/path/commit/515959ffb0053547ed5bc9a416ff38f5537166bb))
* tui with welcome screen ([5a6a465](https://github.com/bniladridas/path/commit/5a6a465119d32eea7f9e68d32c16b3daa2cdb793))
* update playwright and gemini model ([7622903](https://github.com/bniladridas/path/commit/7622903690602502bbacc9d40f80cacf72da800f))
* Vercel deployment validation workflow and script ([f3ca00c](https://github.com/bniladridas/path/commit/f3ca00cd9b5469c2068ee780fefb2ffed6c8a9db))
* workflow_dispatch to all workflows ([39c1a2f](https://github.com/bniladridas/path/commit/39c1a2fd4757ca0b6832b3ec3c4faf9899a7f49c))

# [1.17.0](https://github.com/bniladridas/path/compare/v1.16.5...v1.17.0) (2026-02-28)


### Features

* load api key from ~/.harper.env ([bf1d4e8](https://github.com/bniladridas/path/commit/bf1d4e8488bcdfee37114785ee477baef31355c7))

## [1.16.5](https://github.com/bniladridas/path/compare/v1.16.4...v1.16.5) (2026-02-28)


### Bug Fixes

* **ci:** use valid node image tag ([b9be612](https://github.com/bniladridas/path/commit/b9be6127d8746ac5e6580b4e01302b54b9b49b53))
* conditional webserver ([cfeef0b](https://github.com/bniladridas/path/commit/cfeef0b8e02e383aa6cf21d10a9ba069b3cb8427))
* remove api key ([eebce2a](https://github.com/bniladridas/path/commit/eebce2a88724d0ed35bdbb2ea4f07ae1a86505dc))
* reuse server in playwright ([e163a6c](https://github.com/bniladridas/path/commit/e163a6c52cd41e9666fcb5871d261a1aa56cc147))

## [1.16.4](https://github.com/bniladridas/path/compare/v1.16.3...v1.16.4) (2026-02-27)


### Bug Fixes

* update port from 5000 to 8000 ([e94d9c8](https://github.com/bniladridas/path/commit/e94d9c8c47196c61b6c2b71cc7e802e43deb9a2e))

## [1.16.3](https://github.com/bniladridas/path/compare/v1.16.2...v1.16.3) (2026-02-27)


### Bug Fixes

* align requirements.txt with pyproject.toml ([b084311](https://github.com/bniladridas/path/commit/b08431190871e60dbc1ec266ee242df9c292a28f))

## [1.16.2](https://github.com/bniladridas/path/compare/v1.16.1...v1.16.2) (2026-02-27)


### Bug Fixes

* update readme links and formatting ([f5f2615](https://github.com/bniladridas/path/commit/f5f2615f09b16a67e235ebe12d32a7584eed0625))

## [1.16.1](https://github.com/bniladridas/path/compare/v1.16.0...v1.16.1) (2026-02-27)


### Bug Fixes

* restore table borders and bg ([87952ad](https://github.com/bniladridas/path/commit/87952adc8b48c90a6e53d697e90fa5c6358a0139))
* use css vars and add thead/tbody ([3e99c79](https://github.com/bniladridas/path/commit/3e99c79fbcd6174d7cfd37ca3638626ba1fc2b1d))

# [1.16.0](https://github.com/bniladridas/path/compare/v1.15.1...v1.16.0) (2026-02-27)


### Bug Fixes

* trailing whitespace ([d4b4548](https://github.com/bniladridas/path/commit/d4b4548e4e3a0a95725e7f74866509aacb9b6f20))


### Features

* allow users to add their own gemini api key ([6b8e086](https://github.com/bniladridas/path/commit/6b8e086e2deb974c103e84e2f00f1b853374a824))

## [1.15.1](https://github.com/bniladridas/path/compare/v1.15.0...v1.15.1) (2026-02-21)


### Bug Fixes

* sanitize user input before logging ([0616a4c](https://github.com/bniladridas/path/commit/0616a4c4b36db3d88821b85402b1b7a1e208639b))

# [1.15.0](https://github.com/bniladridas/path/compare/v1.14.1...v1.15.0) (2026-02-21)


### Features

* add tui with welcome screen ([16f1ebf](https://github.com/bniladridas/path/commit/16f1ebfec2b089da882adcafaf9b4c6bb9753b5e))

## [1.14.1](https://github.com/bniladridas/path/compare/v1.14.0...v1.14.1) (2026-02-21)


### Bug Fixes

* use macos-14 runner ([f094d39](https://github.com/bniladridas/path/commit/f094d393a76f83151d000a81046ab5ee44162b93))

# [1.14.0](https://github.com/bniladridas/path/compare/v1.13.7...v1.14.0) (2026-02-21)


### Features

* add rust native binary cli ([c55a621](https://github.com/bniladridas/path/commit/c55a6219ed4fa274c945a08367a14e146a60aa90))

## [1.13.7](https://github.com/bniladridas/path/compare/v1.13.6...v1.13.7) (2026-02-21)


### Bug Fixes

* graceful rate limit handling ([7e3ac16](https://github.com/bniladridas/path/commit/7e3ac16a2a1dce84238d6025676cb49ca8d7eb02))

## [1.13.6](https://github.com/bniladridas/path/compare/v1.13.5...v1.13.6) (2026-02-21)


### Bug Fixes

* add image generation submit handler ([2fb834f](https://github.com/bniladridas/path/commit/2fb834fbd7191eb51a2c9f5169baf81dfe5b1aa2))

## [1.13.5](https://github.com/bniladridas/path/compare/v1.13.4...v1.13.5) (2026-02-21)


### Bug Fixes

* allow conditional import ([c670a92](https://github.com/bniladridas/path/commit/c670a92abcf164d813d66dbdcf46a1825d38cfee))
* move import inside function ([25bb22a](https://github.com/bniladridas/path/commit/25bb22a233cc2e247dbdd7ce11a13a718ccf6d73))

## [1.13.4](https://github.com/bniladridas/path/compare/v1.13.3...v1.13.4) (2026-02-21)


### Bug Fixes

* add human verification keywords ([0ad7f9a](https://github.com/bniladridas/path/commit/0ad7f9a2e0270b636b7a43c94c88b66ecb1a76ab))

## [1.13.3](https://github.com/bniladridas/path/compare/v1.13.2...v1.13.3) (2026-02-19)


### Bug Fixes

* update uv lockfile ([230aef0](https://github.com/bniladridas/path/commit/230aef0b3cbf00116c49385e32d68b8b2aadb023))

## [1.13.2](https://github.com/bniladridas/path/compare/v1.13.1...v1.13.2) (2026-02-19)


### Bug Fixes

* add issues permission for semantic-release ([e5d8b72](https://github.com/bniladridas/path/commit/e5d8b72388f9a0c8980a56781afb48cb746a9379))

## [1.13.1](https://github.com/bniladridas/path/compare/v1.13.0...v1.13.1) (2026-02-19)


### Bug Fixes

* ternary expressions in check-unused ([38d54ec](https://github.com/bniladridas/path/commit/38d54ecce2f4f6f07b0b0ad73682996ba2d403ea))

# [1.13.0](https://github.com/bniladridas/path/compare/v1.12.0...v1.13.0) (2026-01-13)


### Features

* add Python 3.9 support with legacy google-generativeai ([#105](https://github.com/bniladridas/path/issues/105)) ([a6cf1ca](https://github.com/bniladridas/path/commit/a6cf1cac44165f942b877f339b83d2579a235b5c))

# [1.12.0](https://github.com/bniladridas/path/compare/v1.11.6...v1.12.0) (2025-12-12)


### Features

* update playwright and gemini model ([808cabf](https://github.com/bniladridas/path/commit/808cabfe15c15f777f93eae38208790ede2fc1f8))

## [1.11.6](https://github.com/bniladridas/path/compare/v1.11.5...v1.11.6) (2025-10-21)


### Bug Fixes

* update Dockerfile to use app_local.py ([d79f1fb](https://github.com/bniladridas/path/commit/d79f1fb1d9e4cfbdf9a9507b528c8979b9685023))

## [1.11.5](https://github.com/bniladridas/path/compare/v1.11.4...v1.11.5) (2025-10-21)


### Bug Fixes

* update gunicorn CMD to path.app:app ([fdcef07](https://github.com/bniladridas/path/commit/fdcef07ccaed878b444a0ba35a02747e06a43a7a))

## [1.11.4](https://github.com/bniladridas/path/compare/v1.11.3...v1.11.4) (2025-10-21)


### Bug Fixes

* correct FLASK_APP to module format for gunicorn ([3e35d1b](https://github.com/bniladridas/path/commit/3e35d1b8940119abb3047bedcc2377441c49297c))

## [1.11.3](https://github.com/bniladridas/path/compare/v1.11.2...v1.11.3) (2025-10-21)


### Bug Fixes

* remove extra whitespace in vercel.json ([5671f83](https://github.com/bniladridas/path/commit/5671f83cbdcc436b8bfad2d0875aeb46897ade3c))

## [1.11.2](https://github.com/bniladridas/path/compare/v1.11.1...v1.11.2) (2025-10-21)


### Bug Fixes

* suppress DeprecationWarnings in pytest ([4b367c0](https://github.com/bniladridas/path/commit/4b367c08d58bb8a92ca6884d91d4447d22327985))
* update e2e workflow for path/app.py ([5cd6445](https://github.com/bniladridas/path/commit/5cd64452acaacf5dc9b78f22b33b75ff776f7f39))
* update references to app.py in scripts and configs ([634e956](https://github.com/bniladridas/path/commit/634e9564433c90253d92c3f81990bde73bef2812))
* update template/static paths after moving app.py ([4b87cd3](https://github.com/bniladridas/path/commit/4b87cd37d925af0cbda9d319a1acfa1f10e7cfb7))
* update vercel validation workflow for path/app.py ([f0e2347](https://github.com/bniladridas/path/commit/f0e23478ee2b4148718b7fcb89ef50355f68bdae))

## [1.11.1](https://github.com/bniladridas/path/compare/v1.11.0...v1.11.1) (2025-10-21)


### Bug Fixes

* prevent pytest from collecting app routes as tests ([b6328b2](https://github.com/bniladridas/path/commit/b6328b2f7e0ebc3ac19757aef6d0185cb211277a))

# [1.11.0](https://github.com/bniladridas/path/compare/v1.10.25...v1.11.0) (2025-10-21)


### Features

* add google-generativeai for AI features ([0a5c5e0](https://github.com/bniladridas/path/commit/0a5c5e0ff6527b198936c107484f68a359897d5e))

## [1.10.25](https://github.com/bniladridas/path/compare/v1.10.24...v1.10.25) (2025-10-21)


### Bug Fixes

* add deps to pyproject.toml for Vercel ([f06f441](https://github.com/bniladridas/path/commit/f06f441df602e6d8f4ca37cf0c108658ac8aace9))

## [1.10.24](https://github.com/bniladridas/path/compare/v1.10.23...v1.10.24) (2025-10-21)


### Bug Fixes

* add dependencies to pyproject.toml for Vercel ([0a7a634](https://github.com/bniladridas/path/commit/0a7a63406fbabdcc01170990d66a745722db4c3c))

## [1.10.23](https://github.com/bniladridas/path/compare/v1.10.22...v1.10.23) (2025-10-21)


### Bug Fixes

* remove invalid -e from requirements-vercel.txt ([3560862](https://github.com/bniladridas/path/commit/3560862e72c7770344221a227d93a5651d376ac6))

## [1.10.22](https://github.com/bniladridas/path/compare/v1.10.21...v1.10.22) (2025-10-21)


### Bug Fixes

* make google-generativeai import optional for Vercel ([bf79d6e](https://github.com/bniladridas/path/commit/bf79d6e0738c9f1e28da880f223b53043e788b1d))

## [1.10.21](https://github.com/bniladridas/path/compare/v1.10.20...v1.10.21) (2025-10-21)


### Bug Fixes

* remove PYTHONPATH from vercel.json ([6e9d90f](https://github.com/bniladridas/path/commit/6e9d90f4b06af912010f0925af9a24fdfac512e9))

## [1.10.20](https://github.com/bniladridas/path/compare/v1.10.19...v1.10.20) (2025-10-21)


### Bug Fixes

* revert vercel.json to working config ([e44919e](https://github.com/bniladridas/path/commit/e44919e930213567068ddf9b33985251e3a3cbdc))

## [1.10.19](https://github.com/bniladridas/path/compare/v1.10.18...v1.10.19) (2025-10-21)


### Bug Fixes

* correct PROJECT_ROOT for template paths ([8469bd1](https://github.com/bniladridas/path/commit/8469bd161bbb7a4d5abdf1a0b13238c8768adad2))
* update scripts for app.py in root and path/ structure ([6fb1683](https://github.com/bniladridas/path/commit/6fb1683820f6289061f6f24acb157d85e6af5862))
* update workflow for app.py in root ([9438c41](https://github.com/bniladridas/path/commit/9438c41cf97093c52cf75323e3797b616be3d07c))
* use python3.10 runtime for Vercel ([8c45284](https://github.com/bniladridas/path/commit/8c45284485e208626ae96db6eb295e17fb188c9b))
* use python3.11 runtime ([e631d36](https://github.com/bniladridas/path/commit/e631d36bcdc618f872d50849f58807b6efc380f0))

## [1.10.19](https://github.com/bniladridas/path/compare/v1.10.18...v1.10.19) (2025-10-21)


### Bug Fixes

* correct PROJECT_ROOT for template paths ([8469bd1](https://github.com/bniladridas/path/commit/8469bd161bbb7a4d5abdf1a0b13238c8768adad2))
* update scripts for app.py in root and path/ structure ([6fb1683](https://github.com/bniladridas/path/commit/6fb1683820f6289061f6f24acb157d85e6af5862))
* update workflow for app.py in root ([9438c41](https://github.com/bniladridas/path/commit/9438c41cf97093c52cf75323e3797b616be3d07c))
* use python3.11 runtime ([e631d36](https://github.com/bniladridas/path/commit/e631d36bcdc618f872d50849f58807b6efc380f0))

## [1.10.19](https://github.com/bniladridas/path/compare/v1.10.18...v1.10.19) (2025-10-21)


### Bug Fixes

* correct PROJECT_ROOT for template paths ([8469bd1](https://github.com/bniladridas/path/commit/8469bd161bbb7a4d5abdf1a0b13238c8768adad2))
* update scripts for app.py in root and path/ structure ([6fb1683](https://github.com/bniladridas/path/commit/6fb1683820f6289061f6f24acb157d85e6af5862))
* update workflow for app.py in root ([9438c41](https://github.com/bniladridas/path/commit/9438c41cf97093c52cf75323e3797b616be3d07c))
* use python3.11 runtime ([e631d36](https://github.com/bniladridas/path/commit/e631d36bcdc618f872d50849f58807b6efc380f0))

## [1.10.19](https://github.com/bniladridas/path/compare/v1.10.18...v1.10.19) (2025-10-21)


### Bug Fixes

* correct PROJECT_ROOT for template paths ([8469bd1](https://github.com/bniladridas/path/commit/8469bd161bbb7a4d5abdf1a0b13238c8768adad2))
* update scripts for app.py in root and path/ structure ([6fb1683](https://github.com/bniladridas/path/commit/6fb1683820f6289061f6f24acb157d85e6af5862))
* update workflow for app.py in root ([9438c41](https://github.com/bniladridas/path/commit/9438c41cf97093c52cf75323e3797b616be3d07c))

## [1.10.19](https://github.com/bniladridas/path/compare/v1.10.18...v1.10.19) (2025-10-21)


### Bug Fixes

* update scripts for app.py in root and path/ structure ([6fb1683](https://github.com/bniladridas/path/commit/6fb1683820f6289061f6f24acb157d85e6af5862))
* update workflow for app.py in root ([9438c41](https://github.com/bniladridas/path/commit/9438c41cf97093c52cf75323e3797b616be3d07c))

## [1.10.18](https://github.com/bniladridas/path/compare/v1.10.17...v1.10.18) (2025-10-21)


### Bug Fixes

* move app.py to root for Vercel deployment ([32457f0](https://github.com/bniladridas/path/commit/32457f06780c89c3364647fe462dda4aa2ef72ec))

## [1.10.17](https://github.com/bniladridas/path/compare/v1.10.16...v1.10.17) (2025-10-21)


### Bug Fixes

* remove duplicate requirements.txt from path ([4a99054](https://github.com/bniladridas/path/commit/4a99054fcbd1fbe89cd81e4bf38b1962d9f8e8b5))

## [1.10.16](https://github.com/bniladridas/path/compare/v1.10.15...v1.10.16) (2025-10-21)


### Bug Fixes

* use root requirements.txt for Vercel ([69538ab](https://github.com/bniladridas/path/commit/69538abff4fd496abc7095a9dc32fc8d83b60cd1))

## [1.10.15](https://github.com/bniladridas/path/compare/v1.10.14...v1.10.15) (2025-10-21)


### Bug Fixes

* specify requirements path in vercel config ([78ae438](https://github.com/bniladridas/path/commit/78ae4381c86ecc924ff10c186ceca3ca7a198d80))

## [1.10.14](https://github.com/bniladridas/path/compare/v1.10.13...v1.10.14) (2025-10-21)


### Bug Fixes

* add back PYTHONPATH for imports ([a89bedf](https://github.com/bniladridas/path/commit/a89bedfca401538f43e62d69ca70ed1eafd20b61))
* remove PYTHONPATH from vercel config ([1a29c28](https://github.com/bniladridas/path/commit/1a29c281ceccf7ea640851d7a790ca4b3695de4c))
* use python3.9 runtime for Vercel ([4b13d44](https://github.com/bniladridas/path/commit/4b13d444b182b234cdd5c0bdaf594493858d3b9d))

## [1.10.13](https://github.com/bniladridas/path/compare/v1.10.12...v1.10.13) (2025-10-21)


### Bug Fixes

* use python3.11 runtime for Vercel compatibility ([c3665e9](https://github.com/bniladridas/path/commit/c3665e9a76ab30107848458c59a49d527fb08a4f))

## [1.10.12](https://github.com/bniladridas/path/compare/v1.10.11...v1.10.12) (2025-10-21)


### Bug Fixes

* specify python3.12 runtime for Vercel ([5e62482](https://github.com/bniladridas/path/commit/5e624823acea9d9781bb5f9c01290de216d23d0c))

## [1.10.11](https://github.com/bniladridas/path/compare/v1.10.10...v1.10.11) (2025-10-21)


### Bug Fixes

* conditionally import dotenv for local dev ([7ce74a2](https://github.com/bniladridas/path/commit/7ce74a21e5250b01d2c50c80ce911b2bbe31c919))

## [1.10.10](https://github.com/bniladridas/path/compare/v1.10.9...v1.10.10) (2025-10-21)


### Bug Fixes

* conditionally load dotenv for local dev only ([0b266dd](https://github.com/bniladridas/path/commit/0b266ddffaf58b6cdccb1e02aa755d6052cba5f4))

## [1.10.9](https://github.com/bniladridas/path/compare/v1.10.8...v1.10.9) (2025-10-21)


### Bug Fixes

* remove unused import and add dotenv loading ([3455a79](https://github.com/bniladridas/path/commit/3455a79d844ccb8acee1ec6778862079f6b9c556))

## [1.10.8](https://github.com/bniladridas/path/compare/v1.10.7...v1.10.8) (2025-10-21)


### Bug Fixes

* update Jinja2 to fix security vulnerabilities ([4a8d7f2](https://github.com/bniladridas/path/commit/4a8d7f2c496bddfe9d448c29cd66cc81f8cbaee9))

## [1.10.7](https://github.com/bniladridas/path/compare/v1.10.6...v1.10.7) (2025-10-21)


### Bug Fixes

* update root requirements.txt to match path versions ([0c4807e](https://github.com/bniladridas/path/commit/0c4807ea3ab80b4fff46868790bf9cc9ad3f40ba))

## [1.10.6](https://github.com/bniladridas/path/compare/v1.10.5...v1.10.6) (2025-10-21)


### Bug Fixes

* add missing packages to path/requirements.txt ([d92aa16](https://github.com/bniladridas/path/commit/d92aa1646947933c25c12c15d8cc832822081b82))

## [1.10.5](https://github.com/bniladridas/path/compare/v1.10.4...v1.10.5) (2025-10-21)


### Bug Fixes

* remove dotenv dependency for deployment ([8abe84a](https://github.com/bniladridas/path/commit/8abe84a6b3927454f5929a9baf6e97c0cd60caef))

## [1.10.4](https://github.com/bniladridas/path/compare/v1.10.3...v1.10.4) (2025-10-21)


### Bug Fixes

* make dotenv import optional for deployment ([4a6bb76](https://github.com/bniladridas/path/commit/4a6bb766bb7ba468440819dfd3ccd65edb825323))

## [1.10.3](https://github.com/bniladridas/path/compare/v1.10.2...v1.10.3) (2025-10-21)


### Bug Fixes

* update python-dotenv version ([05d835d](https://github.com/bniladridas/path/commit/05d835dda0cd7a9edcba7bb633001c8875e21ec6))

## [1.10.2](https://github.com/bniladridas/path/compare/v1.10.1...v1.10.2) (2025-10-21)


### Bug Fixes

* requests import order and flask_openapi3 imports ([5c4dbb1](https://github.com/bniladridas/path/commit/5c4dbb1562d28e37da294293c36921eb12f19e37))

## [1.10.1](https://github.com/bniladridas/path/compare/v1.10.0...v1.10.1) (2025-10-21)


### Bug Fixes

* sanitize query in logs to prevent log injection ([6804088](https://github.com/bniladridas/path/commit/6804088b40b9da8fb7476b1e5a5512ff8396faba))

# [1.10.0](https://github.com/bniladridas/path/compare/v1.9.0...v1.10.0) (2025-10-21)


### Features

* replace emojis with ANSI colored logging ([ea19fb4](https://github.com/bniladridas/path/commit/ea19fb4bcb5312ef9f8eb83b95201a3846ed505c))

# [1.9.0](https://github.com/bniladridas/path/compare/v1.8.0...v1.9.0) (2025-10-21)


### Features

* add colored ANSI logging to e2e.yml workflow ([7df18e5](https://github.com/bniladridas/path/commit/7df18e5a911c6d088016dd460bad26ede47d7b3d))

# [1.8.0](https://github.com/bniladridas/path/compare/v1.7.0...v1.8.0) (2025-10-21)


### Features

* add logging for Vercel debugging ([064e914](https://github.com/bniladridas/path/commit/064e9142abb782ca0f93571b3f1447977ecb9134))
* add print() with noqa for Vercel logging ([c075883](https://github.com/bniladridas/path/commit/c075883ed33519ca503bd18852f316fa52e8c4d9))

# [1.7.0](https://github.com/bniladridas/path/compare/v1.6.0...v1.7.0) (2025-10-21)


### Features

* add colored ANSI logging to all workflow steps ([844fef6](https://github.com/bniladridas/path/commit/844fef6ac41fd4ab8d11b968e15c306fa1c1f042))

# [1.6.0](https://github.com/bniladridas/path/compare/v1.5.1...v1.6.0) (2025-10-21)


### Features

* add workflow_dispatch to all workflows ([06b89d2](https://github.com/bniladridas/path/commit/06b89d2a4b84ee91136a7f234177b917f177efbd))

## [1.5.1](https://github.com/bniladridas/path/compare/v1.5.0...v1.5.1) (2025-10-21)


### Bug Fixes

* add nosec comments for bandit security warnings ([49daa32](https://github.com/bniladridas/path/commit/49daa3269a43366703ab6b72cd05ec9c4bd9b38b))

# [1.5.0](https://github.com/bniladridas/path/compare/v1.4.1...v1.5.0) (2025-10-21)


### Features

* add OpenAPI spec, versioning, status endpoint ([3359e9c](https://github.com/bniladridas/path/commit/3359e9cd385170ef787831434bcd0fa41c0d7366))

## [1.4.1](https://github.com/bniladridas/path/compare/v1.4.0...v1.4.1) (2025-10-21)


### Bug Fixes

* change app host to 127.0.0.1 for localhost access ([5ddd390](https://github.com/bniladridas/path/commit/5ddd3909ab0cbf8474ae8e2d57a7271f739f73dd))

# [1.4.0](https://github.com/bniladridas/path/compare/v1.3.0...v1.4.0) (2025-10-21)


### Features

* add /status endpoint for API health checks ([6454140](https://github.com/bniladridas/path/commit/645414021b6fd77ca68b7ccae9c41c0848a2369c))

# [1.3.0](https://github.com/bniladridas/path/compare/v1.2.14...v1.3.0) (2025-10-21)


### Features

* enhance OpenAPI spec with models and tags ([76e0343](https://github.com/bniladridas/path/commit/76e034371ec6f10d3a5f4df31bddecc1f98bf2d4))

## [1.2.14](https://github.com/bniladridas/path/compare/v1.2.13...v1.2.14) (2025-10-21)


### Bug Fixes

* use py38 requirements in vercel build simulation ([6d6182d](https://github.com/bniladridas/path/commit/6d6182d90917c93c1ab03196f56d574af8eb3559))

## [1.2.13](https://github.com/bniladridas/path/compare/v1.2.12...v1.2.13) (2025-10-21)


### Bug Fixes

* use py38 requirements in vercel build simulation ([281e0c9](https://github.com/bniladridas/path/commit/281e0c91776b5eddadbb4bf6776c745a58252463))

## [1.2.12](https://github.com/bniladridas/path/compare/v1.2.11...v1.2.12) (2025-10-21)


### Bug Fixes

* add flask-openapi3 to py38 requirements ([b5ce667](https://github.com/bniladridas/path/commit/b5ce6676fd56b6ec3ad354a97a227150b6bdefcd))

## [1.2.11](https://github.com/bniladridas/path/compare/v1.2.10...v1.2.11) (2025-10-21)


### Bug Fixes

* update vercel runtime to 3.9+ for compatibility ([ffca293](https://github.com/bniladridas/path/commit/ffca293c20a42627b7572182a7f14ac97baa53c9))

## [1.2.10](https://github.com/bniladridas/path/compare/v1.2.9...v1.2.10) (2025-10-21)


### Bug Fixes

* update vercel runtime to 3.9+ for compatibility ([71813ef](https://github.com/bniladridas/path/commit/71813ef557c2846a78389f7795667e6fb64096f9))
* use py38 requirements in vercel validation for 3.8 ([1fcae94](https://github.com/bniladridas/path/commit/1fcae94cba5146e7ada5638e8b2a953e53e80ab6))

## [1.2.9](https://github.com/bniladridas/path/compare/v1.2.8...v1.2.9) (2025-10-21)


### Bug Fixes

* update requests to 2.32.4 (2.32.5 doesn't exist) ([b1ccef0](https://github.com/bniladridas/path/commit/b1ccef08ed87f35e4eac76708fba1b0b54ecf984))

## [1.2.8](https://github.com/bniladridas/path/compare/v1.2.7...v1.2.8) (2025-10-21)


### Bug Fixes

* follow redirects in env vars test ([e226f5b](https://github.com/bniladridas/path/commit/e226f5b2cd41242b7fcba7c8f4f392c87f33c183))

## [1.2.7](https://github.com/bniladridas/path/compare/v1.2.6...v1.2.7) (2025-10-21)


### Bug Fixes

* set template and static folders to project root paths ([58da6b3](https://github.com/bniladridas/path/commit/58da6b371b0446a86e50399a1f79820d62292973))

## [1.2.6](https://github.com/bniladridas/path/compare/v1.2.5...v1.2.6) (2025-10-21)


### Bug Fixes

* update python-dotenv for Python 3.8-3.12 compatibility ([9cccfd5](https://github.com/bniladridas/path/commit/9cccfd5b0a4bdc24f0cb819db60164f9d2c7a17f))

## [1.2.5](https://github.com/bniladridas/path/compare/v1.2.4...v1.2.5) (2025-10-21)


### Bug Fixes

* improve route tests and fix yaml linting ([58c94bf](https://github.com/bniladridas/path/commit/58c94bfd973c16a754bfc7517453487a74ebe8a8))

## [1.2.4](https://github.com/bniladridas/path/compare/v1.2.3...v1.2.4) (2025-10-21)


### Bug Fixes

* update config ([6c6a9f3](https://github.com/bniladridas/path/commit/6c6a9f3a9454b9858f13210b25cad67281360dc7))

## [1.2.3](https://github.com/bniladridas/path/compare/v1.2.2...v1.2.3) (2025-10-21)


### Bug Fixes

* update Vercel config for nested path structure ([0cc5a87](https://github.com/bniladridas/path/commit/0cc5a87e31f3967bdb46a4357e27803929ed9b2a))

## [1.2.2](https://github.com/bniladridas/path/compare/v1.2.1...v1.2.2) (2025-10-21)


### Bug Fixes

* update config ([ff67a06](https://github.com/bniladridas/path/commit/ff67a06fc3b2ae8da73644ea5ece86c21c2b70b9))

## [1.2.1](https://github.com/bniladridas/path/compare/v1.2.0...v1.2.1) (2025-10-21)


### Bug Fixes

* update vercel.json with correct runtime configuration ([fb6b634](https://github.com/bniladridas/path/commit/fb6b634fdd23ed9da910dd15373370c80e2738f1))

# [1.2.0](https://github.com/bniladridas/path/compare/v1.1.11...v1.2.0) (2025-10-21)


### Features

* add Vercel deployment validation workflow and script ([ff04f4e](https://github.com/bniladridas/path/commit/ff04f4e121a27edb1d06451b4247447da1475a89))

## [1.1.11](https://github.com/bniladridas/path/compare/v1.1.10...v1.1.11) (2025-10-21)


### Bug Fixes

* simplify Flask app for Vercel compatibility ([cbe3c89](https://github.com/bniladridas/path/commit/cbe3c89f3755949d2c4bd97df9c5d5e9a7e4a1a1))

## [1.1.10](https://github.com/bniladridas/path/compare/v1.1.9...v1.1.10) (2025-10-21)


### Bug Fixes

* let Vercel auto-detect Python version ([35d107d](https://github.com/bniladridas/path/commit/35d107df3ff70e245baa957708c439d3df297d45))

## [1.1.9](https://github.com/bniladridas/path/compare/v1.1.8...v1.1.9) (2025-10-21)


### Bug Fixes

* add Python runtime version to Vercel config ([39ea1ec](https://github.com/bniladridas/path/commit/39ea1ec82bb373443a6ddfd72b10cf21608651e2))

## [1.1.8](https://github.com/bniladridas/path/compare/v1.1.7...v1.1.8) (2025-10-21)


### Bug Fixes

* switch to modern Vercel functions format ([678026e](https://github.com/bniladridas/path/commit/678026ea6e4f4852e4aa3a3a17750b1976a3aadb))

## [1.1.7](https://github.com/bniladridas/path/compare/v1.1.6...v1.1.7) (2025-10-21)


### Bug Fixes

* disable debug mode in test app for security ([fc1b79a](https://github.com/bniladridas/path/commit/fc1b79a530bad0470199a6fe004c5f8af6ad7b37))

## [1.1.6](https://github.com/bniladridas/path/compare/v1.1.5...v1.1.6) (2025-10-21)


### Bug Fixes

* make imports more robust for Vercel deployment ([265901f](https://github.com/bniladridas/path/commit/265901fce4a8fd4cf38ce12a186507aed97dd67e))

## [1.1.5](https://github.com/bniladridas/path/compare/v1.1.4...v1.1.5) (2025-10-21)


### Bug Fixes

* remove api directory and use legacy Vercel config ([cd2e7fb](https://github.com/bniladridas/path/commit/cd2e7fb138b95e8dcce625e8845f62a71ace4914))

## [1.1.4](https://github.com/bniladridas/path/compare/v1.1.3...v1.1.4) (2025-10-20)


### Bug Fixes

* use default Python runtime for Vercel ([530c2d2](https://github.com/bniladridas/path/commit/530c2d293081644d228ccace2102f1c19c18b9e1))

## [1.1.3](https://github.com/bniladridas/path/compare/v1.1.2...v1.1.3) (2025-10-20)


### Bug Fixes

* use valid Python runtime version for Vercel ([d2ca693](https://github.com/bniladridas/path/commit/d2ca693a66c4035844c6b4b7840e7a3648060421))

## [1.1.2](https://github.com/bniladridas/path/compare/v1.1.1...v1.1.2) (2025-10-20)


### Bug Fixes

* add Python runtime config to vercel.json ([ec6777e](https://github.com/bniladridas/path/commit/ec6777e4c569cc03449ed36c4c07c5d8141292b5))

## [1.1.1](https://github.com/bniladridas/path/compare/v1.1.0...v1.1.1) (2025-10-20)


### Bug Fixes

* simplify api/index.py import structure ([efbd22a](https://github.com/bniladridas/path/commit/efbd22a0dba1f99d92e6e420249fdb4254569815))

# [1.1.0](https://github.com/bniladridas/path/compare/v1.0.8...v1.1.0) (2025-10-20)


### Features

* add static file routing for Vercel deployment ([0636a35](https://github.com/bniladridas/path/commit/0636a359c32f6bc047df80ea899b8b31bd0ef389))

## [1.0.8](https://github.com/bniladridas/path/compare/v1.0.7...v1.0.8) (2025-10-20)


### Bug Fixes

* add api/index.py to import from path directory ([2264c89](https://github.com/bniladridas/path/commit/2264c89204366344f1d64cd56c487f005023501c))

## [1.0.7](https://github.com/bniladridas/path/compare/v1.0.6...v1.0.7) (2025-10-20)


### Bug Fixes

* remove api dir and use path for Vercel functions ([09e304e](https://github.com/bniladridas/path/commit/09e304ea82d207513c436bf4a4dfa6c0e91e7038))

## [1.0.6](https://github.com/bniladridas/path/compare/v1.0.5...v1.0.6) (2025-10-20)


### Bug Fixes

* update Vercel config for api directory ([46712fb](https://github.com/bniladridas/path/commit/46712fbb9cdb9a292b12ffd4c67ec8a0b1bdbfc1))

## [1.0.5](https://github.com/bniladridas/path/compare/v1.0.4...v1.0.5) (2025-10-20)


### Bug Fixes

* **vercel:** specify Python runtime version ([7594572](https://github.com/bniladridas/path/commit/7594572be4c4a52e768950d1635ebaa602029f8e))

## [1.0.4](https://github.com/bniladridas/path/compare/v1.0.3...v1.0.4) (2025-10-20)


### Bug Fixes

* **vercel:** resolve conflicting functions and builds config ([5aeff30](https://github.com/bniladridas/path/commit/5aeff30c202985cfc3c452a1563e2c641964547b))

## [1.0.3](https://github.com/bniladridas/path/compare/v1.0.2...v1.0.3) (2025-10-20)


### Bug Fixes

* **vercel:** resolve 404 error after api to path rename ([5f91d8f](https://github.com/bniladridas/path/commit/5f91d8f02ab87cee32362429bd215e63f5a3762b))

## [1.0.2](https://github.com/bniladridas/path/compare/v1.0.1...v1.0.2) (2025-10-20)


### Bug Fixes

* **ci:** prepare deployment files before running tests ([c9c280c](https://github.com/bniladridas/path/commit/c9c280ca877e3356f276004fa293eb3509918036))

## [1.0.1](https://github.com/bniladridas/path/compare/v1.0.0...v1.0.1) (2025-10-20)


### Bug Fixes

* **tests:** update imports from api to path module ([f3d9b69](https://github.com/bniladridas/path/commit/f3d9b698936702a1057d195b603a707503f31f3f))

# 1.0.0 (2025-10-20)


### Bug Fixes

* add build script for dependency installation ([c2c8e49](https://github.com/bniladridas/path/commit/c2c8e49204278515edb0b6781f747917f0ceecc2))
* add current dir to path for app import ([75b9940](https://github.com/bniladridas/path/commit/75b994052fbd23871bce7ae8070f7da3f3402658))
* add explicit python runtime config ([d56e784](https://github.com/bniladridas/path/commit/d56e784189fbaa4d3badcf388f47262d240ac85b))
* add missing dependencies to api requirements ([4ccad3b](https://github.com/bniladridas/path/commit/4ccad3b485b38819d41438148401ec88b9630c71))
* add pip install command to vercel config ([eeebe36](https://github.com/bniladridas/path/commit/eeebe36ddd005081dbe921d2ccdf98394902d591))
* **ci:** add Docker build resilience and fallback options ([9607569](https://github.com/bniladridas/path/commit/960756900c52f9db1a74c18907e89252ce9838d4))
* **ci:** apply Python 3.8 compatibility to all workflows ([bb7e784](https://github.com/bniladridas/path/commit/bb7e784eb296d0e530002c88eb4c69352e841303))
* **ci:** improve Docker health check with better debugging ([bf021a9](https://github.com/bniladridas/path/commit/bf021a94de98fea404d01030538c11e4a01208ee))
* **ci:** replace non-existent GitHub actions ([07065dc](https://github.com/bniladridas/path/commit/07065dc642fe3ec7fc02c54aa069d5f148ed69ac))
* **ci:** simplify automated release workflow ([a165307](https://github.com/bniladridas/path/commit/a16530783ede381f606a7b1b84df7db80ebf969f))
* correct pylint workflow configuration ([29aacd8](https://github.com/bniladridas/path/commit/29aacd843cc02ae147bbb55e1e2dceca2896fc25))
* correct vercel.json schema for build command ([2ba35fb](https://github.com/bniladridas/path/commit/2ba35fbb7117175a80272fd90d3e7c0f6342309c))
* **deps:** adjust Python support to 3.9+ for compatibility ([7d9cb32](https://github.com/bniladridas/path/commit/7d9cb3299b3398aae06891887165521275f40015))
* **deps:** ensure Python 3.8 compatibility ([a312282](https://github.com/bniladridas/path/commit/a31228207a03747ebf93316ce52ec41a0675ef4e))
* **deps:** resolve Flask-Werkzeug conflict for Python 3.8 ([40e28e9](https://github.com/bniladridas/path/commit/40e28e970050e1ceec35698f237be91535718c47))
* **deps:** standardize Python version to 3.10 across project ([c699a76](https://github.com/bniladridas/path/commit/c699a7626841c2b93002aae0c89afbf0779ca103))
* **deps:** update Python 3.8 requirements for compatibility ([14f934c](https://github.com/bniladridas/path/commit/14f934c59920f264bd0f4e2a2220318f8baf4bc1))
* **deps:** update to stable package versions ([96cc4ed](https://github.com/bniladridas/path/commit/96cc4ed8d0cc19fe1507a8e7e77b48926a2071fd))
* **docker:** add app.py entry point for Gunicorn ([8c4f3a1](https://github.com/bniladridas/path/commit/8c4f3a174b5946fb9e8fa2fb5585456442590e78))
* format code with ruff ([ad067b1](https://github.com/bniladridas/path/commit/ad067b1e422fe82b42748e8379ef6967b3a93102))
* format YAML files and fix linting issues ([339f305](https://github.com/bniladridas/path/commit/339f3055491d3cbde46896558c9c3a133c88b7ef))
* implement custom vercel build script ([500e508](https://github.com/bniladridas/path/commit/500e50832cf092aeb84530168b1c069d2714c25d))
* improve e2e test reliability and ci setup ([#44](https://github.com/bniladridas/path/issues/44)) ([e74b2aa](https://github.com/bniladridas/path/commit/e74b2aa267feb4155695ad84bc201df09f839e84))
* improve pylint workflow formatting ([8f011d9](https://github.com/bniladridas/path/commit/8f011d955a9c1ad56a1c14c4985781cbb712941c))
* **lint:** add per-file ignore for AST visitor methods ([a222fc9](https://github.com/bniladridas/path/commit/a222fc955dcda7556b252a9997003daf513c1e81))
* **lint:** resolve ruff warnings and config deprecations ([ca642f8](https://github.com/bniladridas/path/commit/ca642f8906c9af6dde306770738853854097ef00))
* move app and assets to api dir for vercel ([fa52663](https://github.com/bniladridas/path/commit/fa5266327a0c7c732c937d57dcca1c29c3254adc))
* move includefiles inside config in vercel.json ([887040e](https://github.com/bniladridas/path/commit/887040e3a47b41b03a97945f38e2de42907fe68d))
* remove custom install command to fix vercel deps ([89bd217](https://github.com/bniladridas/path/commit/89bd2175a2fdd6bf03dca421da289e06da20607d))
* remove invalid installcommand from vercel.json ([36fc407](https://github.com/bniladridas/path/commit/36fc4071783bc4f7786bc52e0a04c2d9ff45d635))
* remove invalid runtime config ([0a84600](https://github.com/bniladridas/path/commit/0a8460021a77b5746c75373ba5a2b7544c5da9fa))
* rename root app.py to avoid import conflict ([1f6e388](https://github.com/bniladridas/path/commit/1f6e388bdc977ed1aecb555bae88bb54ebcd0d69))
* restore previous changes and update documentation ([3064fa8](https://github.com/bniladridas/path/commit/3064fa8d5ad0960f08e3c528b06937582c0b2420))
* revert vercel.json to include builds for deployment ([1e8685e](https://github.com/bniladridas/path/commit/1e8685e66eb1f1cebe41d308216a377b20a89962))
* **security:** configure Bandit for web app patterns ([60a1b8d](https://github.com/bniladridas/path/commit/60a1b8d22a9438e688462d9e39a77ae5e4f42764))
* **security:** correct Bandit config file format ([ddd01a8](https://github.com/bniladridas/path/commit/ddd01a83164773c12dba35482135077986d4edd0))
* **security:** resolve Bandit B112 warning ([4db5179](https://github.com/bniladridas/path/commit/4db5179bd3dcdea2782770d53dcdbd5243ebad6e))
* **security:** resolve Jinja2 vulnerabilities and pin deps ([63e4350](https://github.com/bniladridas/path/commit/63e4350714e9808ab3fba2473af67bc14ab2ccc2))
* simplify vercel configuration ([a0efa19](https://github.com/bniladridas/path/commit/a0efa1980079ec17d2831bec478a072dca210e4e))
* update build configuration and dependencies ([ece6143](https://github.com/bniladridas/path/commit/ece6143ecb0cc90b88b2eef37307f854c9ba7996))
* update build process for dependency installation ([dc2ff5b](https://github.com/bniladridas/path/commit/dc2ff5b2881bc4efb75d094427d28d995d6ff655))
* update itsdangerous for flask 3.1.2 compatibility ([682d8f1](https://github.com/bniladridas/path/commit/682d8f15d4cf7b98b96ee63d50e761bab81cd17c))
* update requests implementation for vercel ([cd9f8f9](https://github.com/bniladridas/path/commit/cd9f8f99f43f0e8eff2ffe93eaf933d6c8a1f176))
* update requirements and vercel config for deployment ([a6bfaef](https://github.com/bniladridas/path/commit/a6bfaeff4bf28c814004d89cb594dff6dce19115))
* update test imports and app name check ([7565af8](https://github.com/bniladridas/path/commit/7565af80c97ede664eafa8562ffb4aa0971c790b))
* update vercel config and add python runtime ([5fcc423](https://github.com/bniladridas/path/commit/5fcc423419d00001ea9abb6a323e522d2405f9af))
* update vercel config for better python support ([df03ab7](https://github.com/bniladridas/path/commit/df03ab7961db8de6a9298cc78548db07022810d4))
* update vercel config for python 3.11 ([24bf955](https://github.com/bniladridas/path/commit/24bf95593c540a7924ed334968c1872fb550660d))
* update vercel config with explicit python 3.9 runtime ([d7f3c0c](https://github.com/bniladridas/path/commit/d7f3c0c160fa3ddf87c90be7a5d2a55b7462996e))
* update vercel configuration for python dependencies ([7829271](https://github.com/bniladridas/path/commit/7829271626e3ede44bba1b46590adb7dadf7f869))
* update vercel package to version 0.3.2 ([7fdfb83](https://github.com/bniladridas/path/commit/7fdfb8348444e60c9eb0d037d3f2d8f1341ef905))
* update werkzeug and vercel versions for compatibility ([a93c5ee](https://github.com/bniladridas/path/commit/a93c5ee887e2aed7eaa1e8f3b2eb5e11b72833da))
* use @vercel/python@5.7.1 ([1192e4f](https://github.com/bniladridas/path/commit/1192e4f2ed42ef89a95058954b337aa56ed13251))
* use modern vercel config with rewrites ([a911ef3](https://github.com/bniladridas/path/commit/a911ef3acc982c7e70798d4178fadd2b9843723b))


### Features

* add comprehensive unused code detection tools ([323fe72](https://github.com/bniladridas/path/commit/323fe72d78471276e1b10ee3dbe60d40f1d48a85))
* add conventional commit standards and scripts ([376fda1](https://github.com/bniladridas/path/commit/376fda13f5604f646a493c7a105b1f7bb0e61272))
* add conventional commit standards and scripts ([db37a3a](https://github.com/bniladridas/path/commit/db37a3a753078e26156d4795c79a83f1d3c96e49))
* add fully automated release system ([1481216](https://github.com/bniladridas/path/commit/14812167465dfc505f92c2f09bb4f696d42baf24))
* **ci:** add Python 3.8-3.12 matrix testing ([75a4532](https://github.com/bniladridas/path/commit/75a453279dc8020cd54afcf9a4fe61ef9034b1bf))
* **ci:** restore Python 3.8 support with compatibility ([519b97c](https://github.com/bniladridas/path/commit/519b97c7d92c6fa0b6bb177c3c6fdf0eedfb60d0))
* **docker:** add dual registry support (GHCR + Docker Hub) ([396e591](https://github.com/bniladridas/path/commit/396e5912023ab0d41a983ddf52caeea3b4afb99e))
