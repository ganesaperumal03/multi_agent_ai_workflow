from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Multi-Agent AI Workflow"

    LLM_PROVIDER: str = "groq"

    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama3-70b-8192"

    WORKFLOW_ENGINE: str = "langgraph"

    REDIS_URL: str = "redis://localhost:6379"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"

    class Config:
        env_file = ".env"


settings = Settings()