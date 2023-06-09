from pydantic import BaseSettings


class Environment(BaseSettings):
    USERNAME: str
    PASSWORD: str
    DATABASE: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()
