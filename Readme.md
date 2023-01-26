## A simple cmdline tool to backup your github repos
by DQ

### App Info
- written in python3 (native)
- Libs / Mods: requests, pydantic
- Ready 4 Win Mac Lnx

### How to use
- local installation of python (min 3.9) is required<br>
or you can use the docker image / Dockerfile
- set your github creds and paras in config.py<br>
or use envs (GITHUB_USERNAME, GITHUB_API_TOKEN aso.)
``` 
$ pip install -r requirements.txt
$ python ./src/runner.py
$ ls ./data
```
or
```
$ docker run --rm \
  -e GITHUB_USERNAME=YOURUSER \
  -e GITHUB_API_TOKEN=YOURTOKEN \
  -e PYTHONUNBUFFERED=1 \
  -v $PWD:/app/data \
  githubrepobackup:latest