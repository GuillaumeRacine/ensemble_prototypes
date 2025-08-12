from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database
    database_url: str = "postgresql://localhost/present_agent"
    redis_url: str = "redis://localhost:6379"
    
    # OpenAI
    openai_api_key: str = ""
    
    # Instagram
    instagram_verify_token: str = ""
    instagram_access_token: str = ""
    
    # Application
    debug: bool = True
    secret_key: str = "dev-secret-key-change-in-production"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()