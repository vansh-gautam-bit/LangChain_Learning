from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_openrouter import ChatOpenRouter


class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    GOOGLE_API_KEY: str
    HUGGINGFACEHUB_ACCESS_TOKEN: str
   

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()

llm_cohere = ChatOpenRouter(
    model="cohere/north-mini-code:free",
    api_key=settings.OPENROUTER_API_KEY
)