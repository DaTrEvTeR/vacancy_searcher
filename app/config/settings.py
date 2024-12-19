from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.paths import ENV_FILE_PATH


class Settings(BaseSettings):
    BOT__TOKEN: str

    sqlalchemy__database_url: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH, env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
