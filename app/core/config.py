from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Eojin Portfolio Backend"
    API_V1_STR: str = "/api/v1"
    
    # 데이터베이스
    DATABASE_URL: Optional[str] = None
    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "https://eojin.me"]
    
    class Config:
        env_file = ".env"

settings = Settings()