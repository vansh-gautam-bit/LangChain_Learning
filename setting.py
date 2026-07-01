from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_openrouter import ChatOpenRouter
from langchain_google_genai import ChatGoogleGenerativeAI


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

llm_google = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',          #gm.nn.Gemma3_4B   other google model
    api_key=settings.GOOGLE_API_KEY
)