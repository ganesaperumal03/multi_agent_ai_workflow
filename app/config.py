from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Multi-Agent AI Workflow"

    LLM_PROVIDER: str = "groq"

    GROQ_API_KEY: str
    GROQ_MODEL: str = "meta-llama/llama-4-scout-17b-16e-instruct"

    WORKFLOW_ENGINE: str = "orchestrator"

    REDIS_URL: str = "redis://localhost:6379"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"

    class Config:
        env_file = ".env"


settings = Settings()