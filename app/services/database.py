import asyncpg
import asyncio
from typing import List, Dict, Optional
from app.core.config import settings

class DatabaseService:
    def __init__(self):
        self.pool = None
    
    async def connect(self):
        """데이터베이스 연결 풀 생성"""
        try:
            if settings.DATABASE_URL:
                self.pool = await asyncpg.create_pool(
                    settings.DATABASE_URL,
                    min_size=5,
                    max_size=20
                )
                print("✅ Database connected")
            else:
                print("⚠️  DATABASE_URL not set, skipping database connection")
        except Exception as e:
            print(f"⚠️  Database connection failed: {e}")
    
    async def disconnect(self):
        """연결 풀 종료"""
        if self.pool:
            await self.pool.close()
    
    async def record_visit(self, visit_data: dict) -> bool:
        """방문 기록 저장"""
        async with self.pool.acquire() as conn:
            query = """
                INSERT INTO analytics (page_path, ip_address, user_agent, referrer, session_id)
                VALUES ($1, $2, $3, $4, $5)
                RETURNING id
            """
            try:
                result = await conn.fetchval(
                    query,
                    visit_data.get('page_path'),
                    visit_data.get('ip_address'),
                    visit_data.get('user_agent'),
                    visit_data.get('referrer'),
                    visit_data.get('session_id')
                )
                return result is not None
            except Exception as e:
                print(f"Database error: {e}")
                return False
    
    async def get_stats(self) -> Dict:
        """통계 조회"""
        async with self.pool.acquire() as conn:
            # 기본 통계
            basic_stats = await conn.fetchrow("""
                SELECT 
                    COUNT(*) as total_page_views,
                    COUNT(DISTINCT ip_address) as unique_visitors,
                    COUNT(DISTINCT session_id) as total_sessions,
                    COUNT(CASE WHEN created_at >= CURRENT_DATE THEN 1 END) as today_views
                FROM analytics
            """)
            
            # 인기 페이지
            top_pages = await conn.fetch("""
                SELECT page_path, COUNT(*) as count
                FROM analytics 
                WHERE created_at >= NOW() - INTERVAL '7 days'
                GROUP BY page_path 
                ORDER BY count DESC 
                LIMIT 5
            """)
            
            return {
                "total_visitors": basic_stats['unique_visitors'],
                "today_visitors": basic_stats['today_views'],
                "page_views": basic_stats['total_page_views'],
                "total_sessions": basic_stats['total_sessions'],
                "top_pages": [{"page": row['page_path'], "count": row['count']} for row in top_pages]
            }
    
    async def get_daily_stats(self, days: int = 7) -> List[Dict]:
        """일별 통계 조회"""
        async with self.pool.acquire() as conn:
            query = """
                SELECT 
                    DATE(created_at) as date,
                    COUNT(*) as visits,
                    COUNT(DISTINCT ip_address) as unique_visitors
                FROM analytics 
                WHERE created_at >= CURRENT_DATE - INTERVAL '%s days'
                GROUP BY DATE(created_at) 
                ORDER BY date DESC
            """
            rows = await conn.fetch(query, days)
            return [
                {
                    "date": row['date'].isoformat(),
                    "visits": row['visits'],
                    "unique_visitors": row['unique_visitors']
                }
                for row in rows
            ]

# 전역 데이터베이스 서비스 인스턴스
db_service = DatabaseService()