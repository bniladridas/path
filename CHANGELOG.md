# 1.0.0 (2026-04-13)


### Bug Fixes

* align requirements.txt with pyproject.toml ([393145e](https://github.com/bniladridas/path/commit/393145e0ec535a185cdb0bbc38e292d9b327a840))
* allow conditional import ([a23f800](https://github.com/bniladridas/path/commit/a23f800701013e11479dc643faa20decfccd2354))
* api/index.py to import from path directory ([552886d](https://github.com/bniladridas/path/commit/552886d3a97e611a7307a7f80744ce9e6f6ee710))
* back PYTHONPATH for imports ([8748de5](https://github.com/bniladridas/path/commit/8748de5ad70d4f29d4c54ca67c30c82b04eb755d))
* build script for dependency installation ([255ebca](https://github.com/bniladridas/path/commit/255ebca24412dce3a977f476b5d2038e86e0bfaa))
* change app host to 127.0.0.1 for localhost access ([8389a56](https://github.com/bniladridas/path/commit/8389a56c5a88e940cbe28044aa23497a0c2ec478))
* **ci:** apply Python 3.8 compatibility to all workflows ([533916b](https://github.com/bniladridas/path/commit/533916b219c09433ce4aa2767ab3ea11d8ded166))
* **ci:** Docker build resilience and fallback options ([5b74e15](https://github.com/bniladridas/path/commit/5b74e15303f4511721bad8dcb96b19b8c36b0a29))
* **ci:** improve Docker health check with better debugging ([0043d40](https://github.com/bniladridas/path/commit/0043d400436a10589e6a0b3d257b6d525751a380))
* **ci:** prepare deployment files before running tests ([629982b](https://github.com/bniladridas/path/commit/629982bc93fbe5e293abb239b9eca941a04931a0))
* **ci:** replace non-existent GitHub actions ([7506b81](https://github.com/bniladridas/path/commit/7506b81d789207021eef6c90123d6b08dc196000))
* **ci:** simplify automated release workflow ([9599169](https://github.com/bniladridas/path/commit/9599169be8a8a35f404d76445dd4ce9495616789))
* **ci:** use valid node image tag ([a7e1049](https://github.com/bniladridas/path/commit/a7e104911a8ad08c704f0b47676f8147ba29a1be))
* conditional webserver ([ed96186](https://github.com/bniladridas/path/commit/ed96186e82f1f4c7f7f1cc80cdddb3f6f4a01837))
* conditionally import dotenv for local dev ([c06bfcf](https://github.com/bniladridas/path/commit/c06bfcf91b9377bf2bb000eef11536f95e522784))
* conditionally load dotenv for local dev only ([2799842](https://github.com/bniladridas/path/commit/27998421cf203bf67aa9a9f1a40cceba80c89308))
* correct FLASK_APP to module format for gunicorn ([245a417](https://github.com/bniladridas/path/commit/245a41781f15bdaf7ac1ab56a9ae5596f33f1db3))
* correct PROJECT_ROOT for template paths ([1eb0e32](https://github.com/bniladridas/path/commit/1eb0e32a4a0b7c71a97eeebb860e65d4490c424f))
* correct pylint workflow configuration ([f6e6b67](https://github.com/bniladridas/path/commit/f6e6b67c1c1ebbc8ad60392728b728fed5902077))
* correct vercel.json schema for build command ([a94581d](https://github.com/bniladridas/path/commit/a94581d58d0cc232aae5965223f897c522483a9a))
* current dir to path for app import ([4ddbd31](https://github.com/bniladridas/path/commit/4ddbd312b8d53fd320e318398ad3c1c27d415930))
* dependencies to pyproject.toml for Vercel ([dc5dfb5](https://github.com/bniladridas/path/commit/dc5dfb5f484e74493677f60c291395793761df83))
* deps to pyproject.toml for Vercel ([9d242ef](https://github.com/bniladridas/path/commit/9d242ef9ed421ee69bb15a39ff2d733be54d362e))
* **deps:** adjust Python support to 3.9+ for compatibility ([74ab3cd](https://github.com/bniladridas/path/commit/74ab3cd68c149021fab7f6010a0dd28920fc0d05))
* **deps:** ensure Python 3.8 compatibility ([d9f5a81](https://github.com/bniladridas/path/commit/d9f5a81a3db47583ec73c0889c646e284a705ea2))
* **deps:** resolve Flask-Werkzeug conflict for Python 3.8 ([550f333](https://github.com/bniladridas/path/commit/550f33350fe0a9ad5da2bcd5dee2dd56d7e80aa7))
* **deps:** standardize Python version to 3.10 across project ([b984d6e](https://github.com/bniladridas/path/commit/b984d6ee76ff96d31bd39bc488f63a84835c9617))
* **deps:** update Python 3.8 requirements for compatibility ([bf01777](https://github.com/bniladridas/path/commit/bf01777202628b80fb1ef12f755c9ee9cd0bd745))
* **deps:** update to stable package versions ([9c35d61](https://github.com/bniladridas/path/commit/9c35d61258509eacd85dd64a6720af7db5b87088))
* disable debug mode in test app for security ([c9b0039](https://github.com/bniladridas/path/commit/c9b00396edbb217620e7a7e4a27f976daadd84ad))
* **docker:** app.py entry point for Gunicorn ([828a587](https://github.com/bniladridas/path/commit/828a587a77c5c3663a6cf626595064400df82ee2))
* explicit python runtime config ([aceb956](https://github.com/bniladridas/path/commit/aceb956f909f37554d16916d7b225fc3c1c42127))
* flask-openapi3 to py38 requirements ([35d63ed](https://github.com/bniladridas/path/commit/35d63ed842853eea339dfab181ed8b63f5600d59))
* follow redirects in env vars test ([022baa0](https://github.com/bniladridas/path/commit/022baa01b05a7379b435ef7ed998aa595a408867))
* format code with ruff ([671306f](https://github.com/bniladridas/path/commit/671306fb163724e36cac86e5a626b5998da9a4e1))
* format YAML files and fix linting issues ([606bc70](https://github.com/bniladridas/path/commit/606bc70799a368546a8f0fec481a0aa55293ff11))
* graceful rate limit handling ([42d8f7d](https://github.com/bniladridas/path/commit/42d8f7d44b41ecaaccdb9a6fc6a24c731b837446))
* human verification keywords ([76aa0f4](https://github.com/bniladridas/path/commit/76aa0f4996c73a1c10e10c677dcc77d828b64e3a))
* image generation submit handler ([626a3f2](https://github.com/bniladridas/path/commit/626a3f2dc27a11e80567da01ed79f44356b66e12))
* implement custom vercel build script ([226c9b7](https://github.com/bniladridas/path/commit/226c9b7aa7dbb09316c212d05fa0e8b73b4f7bbe))
* improve e2e test reliability and ci setup ([#44](https://github.com/bniladridas/path/issues/44)) ([8373644](https://github.com/bniladridas/path/commit/837364491ccfb046cd1a957be188ee03b4874c12))
* improve pylint workflow formatting ([1ed15f7](https://github.com/bniladridas/path/commit/1ed15f7c032dd142509c2c31b3cb56424423cd27))
* improve route tests and fix yaml linting ([f4d9d7f](https://github.com/bniladridas/path/commit/f4d9d7f57eb7c1ee49ec9728489b8eae027ae26d))
* issues permission for semantic-release ([cc90ade](https://github.com/bniladridas/path/commit/cc90ade7deed3570438eacf79a09fa6260f6bd95))
* let Vercel auto-detect Python version ([740014a](https://github.com/bniladridas/path/commit/740014a0ca849ac4e59dcbad005500aee9f746fc))
* **lint:** per-file ignore for AST visitor methods ([84653ae](https://github.com/bniladridas/path/commit/84653ae3368563c9bacc1fbc052acd5b922a7c61))
* **lint:** resolve ruff warnings and config deprecations ([0637b3a](https://github.com/bniladridas/path/commit/0637b3af25a88ff91aedba4709781e9481bc6cfe))
* make dotenv import optional for deployment ([06adc38](https://github.com/bniladridas/path/commit/06adc38b9115659d9a7bb7594f06c67a5b49e283))
* make google-generativeai import optional for Vercel ([65214f3](https://github.com/bniladridas/path/commit/65214f3141008c2f60e40ac00a8a6cfb16af0e94))
* make imports more robust for Vercel deployment ([b8719fa](https://github.com/bniladridas/path/commit/b8719fad652468e47fa30608954b39724fd44464))
* missing dependencies to api requirements ([2f1a74e](https://github.com/bniladridas/path/commit/2f1a74ebe30b7664a8c989ed2414ae4b13a7b059))
* missing packages to path/requirements.txt ([459af53](https://github.com/bniladridas/path/commit/459af53b62b39e85f104054fa9da2376413360cb))
* move app and assets to api dir for vercel ([51b9c5f](https://github.com/bniladridas/path/commit/51b9c5f58c1b3fef36739207514680f725673c3d))
* move app.py to root for Vercel deployment ([376b90a](https://github.com/bniladridas/path/commit/376b90a7d92096a5b4c4439060e6cbc33bdb440f))
* move import inside function ([53f7909](https://github.com/bniladridas/path/commit/53f7909cbb10b5f766dcd78b4fefd1b0b9b72c16))
* move includefiles inside config in vercel.json ([df2c73e](https://github.com/bniladridas/path/commit/df2c73ecd7d019057024237c9ebf3dfb2a5cb67d))
* nosec comments for bandit security warnings ([731966c](https://github.com/bniladridas/path/commit/731966cbb81f12e9e5ef87ce559dcd4a28c3a388))
* pip install command to vercel config ([0a81501](https://github.com/bniladridas/path/commit/0a81501b2b7515e237a82dcfb87a01c59a090c76))
* prevent pytest from collecting app routes as tests ([b998f25](https://github.com/bniladridas/path/commit/b998f2564bce5a21e07aafe28389da83d4e3ca6d))
* Python runtime config to vercel.json ([b50cc0d](https://github.com/bniladridas/path/commit/b50cc0d23024c52f1c0042e2eb6a612c92751151))
* Python runtime version to Vercel config ([7ddfcc9](https://github.com/bniladridas/path/commit/7ddfcc9c906b09a59edc3f80a8a4f9206537370c))
* remove api dir and use path for Vercel functions ([f77fb55](https://github.com/bniladridas/path/commit/f77fb552387b779b8894e2ee8c05e20e5db9661d))
* remove api directory and use legacy Vercel config ([8cf2e0a](https://github.com/bniladridas/path/commit/8cf2e0a37ae0e0435cbbcf445eb8b2bdebd7af65))
* remove api key ([c5c970a](https://github.com/bniladridas/path/commit/c5c970aa81d74dc3ba04c3b09190e1b53d03d5a1))
* remove custom install command to fix vercel deps ([9737bb6](https://github.com/bniladridas/path/commit/9737bb67aab04c8e81ca667665a35c69ff975bbe))
* remove dotenv dependency for deployment ([a21f729](https://github.com/bniladridas/path/commit/a21f72973babb08dbb2797d4e95dd23ef16f30cc))
* remove duplicate requirements.txt from path ([16fa188](https://github.com/bniladridas/path/commit/16fa188b3b582c7240b7fa0adcc9a38191c02a2b))
* remove extra whitespace in vercel.json ([d1d65d1](https://github.com/bniladridas/path/commit/d1d65d1bdb0044d0f2f21d0412cb90cc1952be64))
* remove invalid -e from requirements-vercel.txt ([3c689c0](https://github.com/bniladridas/path/commit/3c689c06cb92d1548a38ee06caba1b424c770d0e))
* remove invalid installcommand from vercel.json ([0f4ef7f](https://github.com/bniladridas/path/commit/0f4ef7f19e3416c87440b494b8924b0f12a59eb9))
* remove invalid runtime config ([c3e264f](https://github.com/bniladridas/path/commit/c3e264f9da391f8ae69d8b41941ab338f3ec04ba))
* remove PYTHONPATH from vercel config ([b585554](https://github.com/bniladridas/path/commit/b5855541d36850159a74c6c88af74280ca9d01db))
* remove PYTHONPATH from vercel.json ([62c414f](https://github.com/bniladridas/path/commit/62c414f09eaad3205d1026c9dd92ce26fc4e586f))
* remove unused import and dotenv loading ([cb278c3](https://github.com/bniladridas/path/commit/cb278c388d461eb38b2bdb28bb67a90e27218ef3))
* rename root app.py to avoid import conflict ([b7f9e8c](https://github.com/bniladridas/path/commit/b7f9e8c68e2afa7f7955f5bb60f1ca4367a53343))
* requests import order and flask_openapi3 imports ([54c9db9](https://github.com/bniladridas/path/commit/54c9db92fbc4e13b3084dc248ceab155987a91f4))
* restore previous changes and update documentation ([d01bfeb](https://github.com/bniladridas/path/commit/d01bfeb4af4716245fd367f5a33c84512a97baf8))
* restore table borders and bg ([87d6caf](https://github.com/bniladridas/path/commit/87d6caf5b083851c2156cba8a2500539327b58fd))
* reuse server in playwright ([f864272](https://github.com/bniladridas/path/commit/f864272577f91621c534959de74b71bdd3796176))
* revert vercel.json to include builds for deployment ([60df4a4](https://github.com/bniladridas/path/commit/60df4a48edb7a79472af788c78454e809da7974a))
* revert vercel.json to working config ([a2ea339](https://github.com/bniladridas/path/commit/a2ea33946087cb4c6e03b8f3620b0820fc58f0e1))
* sanitize query in logs to prevent log injection ([8c140c1](https://github.com/bniladridas/path/commit/8c140c166b84de103b895299f5b62665451e2994))
* sanitize user input before logging ([742ce06](https://github.com/bniladridas/path/commit/742ce06c4b842f4d9d8e601dea687c6f9d0404f8))
* **security:** configure Bandit for web app patterns ([cc594ba](https://github.com/bniladridas/path/commit/cc594ba1bc71a6910d19b3bbb0bc95e038d988c0))
* **security:** correct Bandit config file format ([3dd8ae9](https://github.com/bniladridas/path/commit/3dd8ae91398b035714bc3a12551cd23b6a8106b2))
* **security:** resolve Bandit B112 warning ([ae957d6](https://github.com/bniladridas/path/commit/ae957d6fdbeaf93eab5655978c5939a9de507fb4))
* **security:** resolve Jinja2 vulnerabilities and pin deps ([13452be](https://github.com/bniladridas/path/commit/13452bef398838f9dc25152df11cb6035934c00d))
* set template and static folders to project root paths ([777045a](https://github.com/bniladridas/path/commit/777045a638431ba6a54788ad958a33c852fa0c8a))
* simplify api/index.py import structure ([475b5a7](https://github.com/bniladridas/path/commit/475b5a716a937c0a19a8c4ebbd08c661d0941870))
* simplify Flask app for Vercel compatibility ([1aca726](https://github.com/bniladridas/path/commit/1aca726190c80df860e903510fc4b8ad1ef8c8f2))
* simplify vercel configuration ([8568ec7](https://github.com/bniladridas/path/commit/8568ec70a18c9f9c0a15c77444512137d7457a40))
* specify python3.12 runtime for Vercel ([206ac62](https://github.com/bniladridas/path/commit/206ac621ff311faf9ebaaa6481b01856bc642913))
* specify requirements path in vercel config ([d314b94](https://github.com/bniladridas/path/commit/d314b94ea3aa954d24501956323c9e95fbb5120e))
* suppress DeprecationWarnings in pytest ([a30ca53](https://github.com/bniladridas/path/commit/a30ca533f52224603e3b83cf660ab478c383ba50))
* switch to modern Vercel functions format ([7c30620](https://github.com/bniladridas/path/commit/7c30620c7a59b3fa7dc8739a00856f9f66925b28))
* ternary expressions in check-unused ([504379a](https://github.com/bniladridas/path/commit/504379afcaaba67e60d94dc59b430c8cd627ea89))
* **tests:** update imports from api to path module ([af24a8d](https://github.com/bniladridas/path/commit/af24a8d94e956ec5202a5a50b65fd088903835b9))
* trailing whitespace ([6776547](https://github.com/bniladridas/path/commit/67765477693bd94176707aa8ecd6fc0ec8dbbff2))
* update build configuration and dependencies ([c0b1cb6](https://github.com/bniladridas/path/commit/c0b1cb6eb65f12139a929431638eed3d2575f482))
* update build process for dependency installation ([66313fa](https://github.com/bniladridas/path/commit/66313fade27182a0b5f70f9ce955fe1253a39c4a))
* update config ([c9605fb](https://github.com/bniladridas/path/commit/c9605fb02a736886136903d344c91f8582f07fc2))
* update config ([0dec89b](https://github.com/bniladridas/path/commit/0dec89b281c9d273ca068eeecca592f1778c600a))
* update Dockerfile to use app_local.py ([5f9d69e](https://github.com/bniladridas/path/commit/5f9d69e87a1db281600c45969a5003041e041523))
* update e2e workflow for path/app.py ([266a68a](https://github.com/bniladridas/path/commit/266a68ab3b578c6df0db60757a16c7fa2b776811))
* update flask and requests to fix vulnerabilities ([4679d28](https://github.com/bniladridas/path/commit/4679d28d30cae7557fe39e3f7006462bbb8a5d5a))
* update gunicorn CMD to path.app:app ([9b347a2](https://github.com/bniladridas/path/commit/9b347a2c6c451588a2734c262cd04c26a52f7de9))
* update itsdangerous for flask 3.1.2 compatibility ([f1f3e5f](https://github.com/bniladridas/path/commit/f1f3e5f469402b2dd0882d388a4387ee7f5f053f))
* update Jinja2 to fix security vulnerabilities ([ab522d5](https://github.com/bniladridas/path/commit/ab522d5801541757b3a761021aaa8881e740d1c7))
* update port from 5000 to 8000 ([6e34201](https://github.com/bniladridas/path/commit/6e3420104ea87046c0e69a9b453f73088fda643a))
* update python-dotenv for Python 3.8-3.12 compatibility ([2e3f1a7](https://github.com/bniladridas/path/commit/2e3f1a7321bbe7022554453dcc710006288c59d6))
* update python-dotenv version ([83824d8](https://github.com/bniladridas/path/commit/83824d837ed98a074753a63b9a1c05a9c6ec8236))
* update readme links and formatting ([3f3ed80](https://github.com/bniladridas/path/commit/3f3ed80b6d5febb738038f028574ee480e404b54))
* update references to app.py in scripts and configs ([1b56a66](https://github.com/bniladridas/path/commit/1b56a66112743a0d4556793b917c209bfc50e2d9))
* update requests implementation for vercel ([14f9f9b](https://github.com/bniladridas/path/commit/14f9f9b6537db449457fe3f59358a571a761b962))
* update requests to 2.32.4 (2.32.5 doesn't exist) ([84d120f](https://github.com/bniladridas/path/commit/84d120ffbf08db7e66d529c00bacf81d15e844b8))
* update requirements and vercel config for deployment ([688e470](https://github.com/bniladridas/path/commit/688e470fedb85440e498ad8cd2e7d7fed5255109))
* update root requirements.txt to match path versions ([4a5b0a6](https://github.com/bniladridas/path/commit/4a5b0a685d59a36bcee1bd2093112a00b7ab4efa))
* update scripts for app.py in root and path/ structure ([41293a4](https://github.com/bniladridas/path/commit/41293a452dd7e0115614628442d84cd24c602735))
* update template/static paths after moving app.py ([26bbc88](https://github.com/bniladridas/path/commit/26bbc8838d50e5657c7c4594e6a9a5be9bd4e26a))
* update test imports and app name check ([a7544d2](https://github.com/bniladridas/path/commit/a7544d27b7746df2226a89d39f824f7527eff842))
* update uv lockfile ([b0d9ee5](https://github.com/bniladridas/path/commit/b0d9ee5ab50f9daa74917808a2da77c6480f03b9))
* update vercel config and python runtime ([947e3ed](https://github.com/bniladridas/path/commit/947e3ed73acdad7366e043935b89ae2291d50d89))
* update Vercel config for api directory ([2983c9b](https://github.com/bniladridas/path/commit/2983c9b7bdfcd1d54e1a00cfb3444d0fe51c2267))
* update vercel config for better python support ([8cd8842](https://github.com/bniladridas/path/commit/8cd8842650677ddb4809a181a5e7a354c8a2ca09))
* update Vercel config for nested path structure ([13be2f2](https://github.com/bniladridas/path/commit/13be2f2a6c69defbb628aeccb5da7312aa8be878))
* update vercel config for python 3.11 ([fb3fd49](https://github.com/bniladridas/path/commit/fb3fd491fc653bb66bd461310d08dbb614b27b3e))
* update vercel config with explicit python 3.9 runtime ([78fb927](https://github.com/bniladridas/path/commit/78fb927df605f7dcb8c5db1f07a6e16b8932f5da))
* update vercel configuration for python dependencies ([a1f095a](https://github.com/bniladridas/path/commit/a1f095a5490b6d1f77c40e2dc2fa0cf3438be26e))
* update vercel package to version 0.3.2 ([b39b651](https://github.com/bniladridas/path/commit/b39b651371619e2cf2b55ea5da87ea2cd0495e61))
* update vercel runtime to 3.9+ for compatibility ([5d1564e](https://github.com/bniladridas/path/commit/5d1564ec268e7233e58b60c17e9a7a3f8e202034))
* update vercel runtime to 3.9+ for compatibility ([46689ef](https://github.com/bniladridas/path/commit/46689ef08e669ef3213234452b25dac8927fc28c))
* update vercel validation workflow for path/app.py ([e1613e1](https://github.com/bniladridas/path/commit/e1613e1eeaa4d6ae3ab862702ddb63c082d353e6))
* update vercel.json with correct runtime configuration ([6635607](https://github.com/bniladridas/path/commit/66356076c741d3c6fadf46dc9055b91374c035fb))
* update werkzeug and vercel versions for compatibility ([8deda44](https://github.com/bniladridas/path/commit/8deda44daac13196f61e8b0ae202bfa0ff41b7c4))
* update workflow for app.py in root ([b137738](https://github.com/bniladridas/path/commit/b1377387a9315719b83dfb7e07522b662cef1409))
* use @vercel/python@5.7.1 ([8212199](https://github.com/bniladridas/path/commit/821219915e2a9e1dbb937c6924c493cf787c3082))
* use css vars and thead/tbody ([c968908](https://github.com/bniladridas/path/commit/c968908c19ebda4eab570d6ad2e65242b4b61fd7))
* use default Python runtime for Vercel ([d55f691](https://github.com/bniladridas/path/commit/d55f69130b90264abac12369b5cd4cc22fe30414))
* use macos-14 runner ([44ec53d](https://github.com/bniladridas/path/commit/44ec53d85fa1a9711fda34f265147f10bddb43a3))
* use modern vercel config with rewrites ([0205bf7](https://github.com/bniladridas/path/commit/0205bf7427b562b43b3fe998ba23297315ca2747))
* use py38 requirements in vercel build simulation ([d267ef7](https://github.com/bniladridas/path/commit/d267ef76b1357dd3c5b5518e0be1a2fdf0b9b33c))
* use py38 requirements in vercel build simulation ([198f10a](https://github.com/bniladridas/path/commit/198f10ad2f71e98ca597743fd75b31a5dd8b50b2))
* use py38 requirements in vercel validation for 3.8 ([d89e04e](https://github.com/bniladridas/path/commit/d89e04eb253a8d990b6abe35164d8fff31054501))
* use python3.10 runtime for Vercel ([20e764d](https://github.com/bniladridas/path/commit/20e764dc092565e8dd01006a3e224ba98c451b2a))
* use python3.11 runtime ([7583ded](https://github.com/bniladridas/path/commit/7583dedb4b6eed41b42cc2e1a245792c0c67b389))
* use python3.11 runtime for Vercel compatibility ([0569c70](https://github.com/bniladridas/path/commit/0569c7043ff6bec81c0ede7886ffcb8f70c05614))
* use python3.9 runtime for Vercel ([3aa81eb](https://github.com/bniladridas/path/commit/3aa81ebcf07f95b61f8dcc9345338bfb116d9723))
* use root requirements.txt for Vercel ([624e710](https://github.com/bniladridas/path/commit/624e71057c42a70a314b12f04a0e9177dd3f4753))
* use valid Python runtime version for Vercel ([6f3ec44](https://github.com/bniladridas/path/commit/6f3ec443b5201cefbdd345a7692fd8ca6fe9a765))
* **vercel:** resolve 404 error after api to path rename ([e5c2cf0](https://github.com/bniladridas/path/commit/e5c2cf059ffd45341d9a355808b93fa2082beb9f))
* **vercel:** resolve conflicting functions and builds config ([97715f8](https://github.com/bniladridas/path/commit/97715f8aa01b0cadf08a5e0f6232320ada3fdae5))
* **vercel:** specify Python runtime version ([d68751e](https://github.com/bniladridas/path/commit/d68751ef6af25626ab4bcd3e55a0f8d5ddccd6cd))


### Features

* /status endpoint for API health checks ([707ead9](https://github.com/bniladridas/path/commit/707ead9df7ebf504e07d3d69e750389aff537615))
* allow users to their own gemini api key ([21fe6e6](https://github.com/bniladridas/path/commit/21fe6e650b4baf4bd0c280da3e602627b6d1a581))
* **ci:** Python 3.8-3.12 matrix testing ([135f9d7](https://github.com/bniladridas/path/commit/135f9d7cdc77314eb8e0b88910df1c389d7df9a7))
* **ci:** restore Python 3.8 support with compatibility ([c5e3925](https://github.com/bniladridas/path/commit/c5e3925a1f3ca5e7b810a876b37e5ec0075f84db))
* colored ANSI logging to all workflow steps ([2d67b98](https://github.com/bniladridas/path/commit/2d67b983ac3c7deb110edb1f43412e03b0e63eb7))
* colored ANSI logging to e2e.yml workflow ([34f7deb](https://github.com/bniladridas/path/commit/34f7deb5e34e298dc2b4ed99616999ed75c0d79a))
* comprehensive unused code detection tools ([0160660](https://github.com/bniladridas/path/commit/016066014f210f4660980674804071bdd928f14f))
* conventional commit standards and scripts ([6ee5ee9](https://github.com/bniladridas/path/commit/6ee5ee94f847478db38a7d3fc0dc31a9347a90e4))
* conventional commit standards and scripts ([a23797a](https://github.com/bniladridas/path/commit/a23797a8ebfe63b247582daff1f26f4321133212))
* **docker:** dual registry support (GHCR + Docker Hub) ([9ff7120](https://github.com/bniladridas/path/commit/9ff712043bfe5c6938aa6df57842a28b37fc662a))
* enhance OpenAPI spec with models and tags ([2018c36](https://github.com/bniladridas/path/commit/2018c36e381571e165f46f08585a04589dc16332))
* fully automated release system ([75b6f66](https://github.com/bniladridas/path/commit/75b6f661933fe82e8eabcfc1e298029c36ac6787))
* google-generativeai for AI features ([481a9e7](https://github.com/bniladridas/path/commit/481a9e7f66a0ec086f2f98ef251b76a533f29c27))
* load api key from ~/.harper.env ([ed727b8](https://github.com/bniladridas/path/commit/ed727b898651a7e4676aa4a2306f2138f4623aee))
* logging for Vercel debugging ([808b75e](https://github.com/bniladridas/path/commit/808b75eece35be0ea47d5c91fd39bd7e1bab28f2))
* OpenAPI spec, versioning, status endpoint ([d490f8f](https://github.com/bniladridas/path/commit/d490f8f088d213eb9029b947ae3f4a8bd25182f4))
* print() with noqa for Vercel logging ([9901381](https://github.com/bniladridas/path/commit/9901381802ab66479793b8ab3d9c10ffac391d8d))
* Python 3.9 support with legacy google-generativeai ([#105](https://github.com/bniladridas/path/issues/105)) ([9e5dd6f](https://github.com/bniladridas/path/commit/9e5dd6fe3345e5aa9611c6ed5b836936fa85421d))
* replace emojis with ANSI colored logging ([b60ce7a](https://github.com/bniladridas/path/commit/b60ce7a06bbf96cb36dbc6fe952a5186a1eb3630))
* rust native binary cli ([d8857cb](https://github.com/bniladridas/path/commit/d8857cb353ecc277c5b54f242fa0f1c892b808d8))
* static file routing for Vercel deployment ([5c1af45](https://github.com/bniladridas/path/commit/5c1af45ef7e1204f7974e3e3272ddfd409bcdf3f))
* tui with welcome screen ([0a4061b](https://github.com/bniladridas/path/commit/0a4061b70a82fe87810906c5275804dc01c6544c))
* update playwright and gemini model ([7b3e854](https://github.com/bniladridas/path/commit/7b3e854ed81e289a7b238c3a5b5dd608b481979d))
* Vercel deployment validation workflow and script ([9be9d16](https://github.com/bniladridas/path/commit/9be9d16f3639c1cb0ff6e59be84de79dd98a1153))
* workflow_dispatch to all workflows ([13e492b](https://github.com/bniladridas/path/commit/13e492b76a224f984b89743e89d19bfb931d8e85))

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
