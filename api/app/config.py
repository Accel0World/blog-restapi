from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):

    postgres_user: str = "PanDoRa_s-AcToR"
    postgres_password: str = "nacxc5&EB&pSz__128"
    postgres_db: str = "blog_db"
    postgres_host: str = "postgres"
    postgres_port: int = 5432

    postgres_dsn: PostgresDsn = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

    class Config:
        pass
        # pass for now!!!


settings = Settings()
