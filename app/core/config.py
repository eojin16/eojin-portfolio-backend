from pydantic import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "EoJin Portfolio Backend"
    API_V1_STR: str = "/api/v1"

    # 데이터베이스
    DATABASE_URL: Optional[str] = None
    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None

    # Redis (optional for local development)
    REDIS_URL: str = "redis://localhost:6379"

    # Kafka (optional for local development)
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"

    # CORS - 문자열로 받아서 리스트로 변환
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://eojin.me"
    ]

    class Config:
        env_file = ".env"

settings = Settings()