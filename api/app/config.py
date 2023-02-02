from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):

    # postgres_user: str
    # postgres_password: str
    # postgres_db: str
    # postgres_host: str
    # postgres_port: int

    postgres_dsn: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

print(settings.postgres_dsn)
