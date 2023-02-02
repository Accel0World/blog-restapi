

class Settings():
    postgres_user: str = "PanDoRa_s-AcToR"
    postgres_password: str = "nacxc5&EB&pSz__128"
    postgres_db: str = "blog_db"
    postgres_host: str = "postgres"
    postgres_port: int = 5432


settings = Settings()
print(settings.postgres_db)
