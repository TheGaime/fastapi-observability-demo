from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Observability Demo"
    app_env: str = "dev"
    app_version: str = "0.1.0"
    log_level: str = "INFO"
    metrics_enabled: bool = True
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
