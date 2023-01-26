## A simple cmdline tool to backup your github repos
### by DQ
<br>

### App Info
- written in python3 (native)
- Libs / Mods: requests, pydantic
- Ready 4 Win Mac Lnx

### How to use
- local installation of python (min 3.9) is required<br>
or you can use the docker image / Dickerfile
- set your github creds and paras in config.py<br>
or use envs (GITHUB_USERNAME, GITHUB_API_TOKEN aso.)
``` 
$ pip install -r requirements.txt
$ python ./src/runner.py
$ ls ./data