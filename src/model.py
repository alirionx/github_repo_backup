from pydantic import BaseModel
from typing import Literal

class AppConfig(BaseModel):
  github_username: str 
  github_api_version: str | None = "2022-11-28"
  github_api_token: str 
  backup_format: Literal["zipball", "tarball"] | None = "zipball"
  backup_target_path: str | None = "./data"

