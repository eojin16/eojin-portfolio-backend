from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "EoJin Portfolio Backend"
    API_V1_STR: str = "/api/v1"
    
    # 데이터베이스
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    
    # CORS - 문자열로 받아서 리스트로 변환
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000", 
        "https://eojin.me"
    ]
    
    class Config:
        env_file = ".env"

settings = Settings()