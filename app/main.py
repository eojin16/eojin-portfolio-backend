from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api import analytics
from app.services.database import db_service
from app.services.redis_service import redis_service
from app.services.kafka_service import kafka_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 실행
    print("🚀 Starting FastAPI backend server...")
    await db_service.connect()
    await redis_service.connect()
    await kafka_service.connect()
    print("✅ All services connected!")
    
    yield
    
    # 종료 시 실행
    print("🛑 Shutting down FastAPI backend server...")
    await db_service.disconnect()
    await redis_service.disconnect()
    await kafka_service.disconnect()
    print("✅ All services disconnected!")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="김어진 포트폴리오 백엔드 API",
    lifespan=lifespan
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(
    analytics.router,
    prefix=f"{settings.API_V1_STR}/analytics",
    tags=["analytics"]
)

@app.get("/")
async def root():
    return {
        "message": "🚀 Eojin Portfolio Backend API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "services": {
            "database": "connected",
            "redis": "connected", 
            "kafka": "connected"
        }
    }