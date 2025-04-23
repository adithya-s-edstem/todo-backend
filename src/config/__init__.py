import os

class Config:
    def __init__(self):
        self.database_host = os.environ.get("DATABASE_HOST", "localhost")
        self.database_port = os.environ.get("DATABASE_PORT", "5432")
        self.database_name = os.environ.get("DATABASE_NAME", "tododb")
        self.database_user = os.environ.get("DATABASE_USER", "postgres")
        self.database_password = os.environ.get("DATABASE_PASSWORD", "postgres")

    @property
    def get_sqlalchemy_settings(self):
        sqlalchemy_database_url = f"postgresql://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"
        sqlalchemy_settings = {
            "SQLALCHEMY_DATABASE_URI": sqlalchemy_database_url,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }

        return sqlalchemy_settings

config = Config()