import redis
import json
import asyncio
from typing import Optional, Dict, Any
from app.core.config import settings

class RedisService:
    def __init__(self):
        self.redis_client = None
    
    async def connect(self):
        """Redis 연결"""
        try:
            self.redis_client = redis.from_url(
                settings.REDIS_URL,
                decode_responses=True
            )
            # Test connection
            self.redis_client.ping()
            print("✅ Redis connected")
        except Exception as e:
            print(f"⚠️  Redis connection failed: {e}")
            self.redis_client = None
    
    async def disconnect(self):
        """Redis 연결 종료"""
        if self.redis_client:
            await self.redis_client.close()
    
    async def get_cached_stats(self) -> Optional[Dict]:
        """캐시된 통계 조회"""
        try:
            cached_data = self.redis_client.get("stats:main")
            if cached_data:
                return json.loads(cached_data)
        except Exception as e:
            print(f"Redis error: {e}")
        return None
    
    async def cache_stats(self, stats: Dict, ttl: int = 30):
        """통계 캐시 저장"""
        try:
            self.redis_client.setex(
                "stats:main",
                ttl,
                json.dumps(stats, default=str)
            )
        except Exception as e:
            print(f"Redis error: {e}")
    
    async def increment_page_view(self, page_path: str):
        """페이지 뷰 카운트 증가"""
        try:
            self.redis_client.incr(f"pageview:{page_path}")
        except Exception as e:
            print(f"Redis error: {e}")

# 전역 Redis 서비스 인스턴스
redis_service = RedisService()