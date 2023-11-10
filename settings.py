from functools import lru_cache
from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
    env_name: str = Field(..., env="ENV_NAME")
    hostname: str = Field(..., env="HOSTNAME")
    port: str = Field(..., env="PORT")

    database_hostname: str = Field(..., env="DATABASE_HOSTNAME")
    database_port: str = Field(..., env="DATABASE_PORT")
    database_username: str = Field(..., env="DATABASE_USERNAME")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_name: str = Field(..., env="DATABASE_NAME")

    class Config:
        env_file = "../.env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
