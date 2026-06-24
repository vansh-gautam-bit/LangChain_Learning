from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    GOOGLE_API_KEY: str
    HUGGINGFACEHUB_ACCESS_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()