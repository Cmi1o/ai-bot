from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    mistralai_token: SecretStr
    redis_url: SecretStr

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', case_sensitive=False
    )


settings = Settings()  # type: ignore
