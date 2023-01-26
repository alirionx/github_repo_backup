#-Your individual config params here----

your_data = {
  "github_username": "MYUSER",
  "github_api_token": "YOURTOKEN", 
  "backup_format": "zipball",
  "backup_target_path": "./data"
}

#---------------------------------------
from model import AppConfig
myConfig = AppConfig(**your_data)

#-Config via Envs-----------------------
import os
for key, val in myConfig.dict().items():
  env = key.upper()
  if os.environ.get(env):
    try:
      setattr(myConfig, key, os.environ.get(env))
    except Exception as e:
      print(e)

#---------------------------------------