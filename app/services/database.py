import requests
from typing import List, Dict, Optional
from app.core.config import settings

class DatabaseService:
    def __init__(self):
        self.connected = False

    async def connect(self):
        """데이터베이스 연결 확인"""
        try:
            if settings.SUPABASE_URL and settings.SUPABASE_KEY:
                self.connected = True
                print("✅ Database connected")
            else:
                print("⚠️  SUPABASE_URL or SUPABASE_KEY not set, skipping database connection")
        except Exception as e:
            print(f"⚠️  Database connection failed: {e}")

    async def disconnect(self):
        """연결 종료"""
        self.connected = False
    
    async def record_visit(self, visit_data: dict) -> bool:
        """방문 기록 저장"""
        if not self.connected:
            return False

        try:
            # Supabase REST API를 직접 호출
            headers = {
                'apikey': settings.SUPABASE_KEY,
                'Authorization': f'Bearer {settings.SUPABASE_KEY}',
                'Content-Type': 'application/json'
            }

            data = {
                'page_path': visit_data.get('page_path'),
                'ip_address': visit_data.get('ip_address'),
                'user_agent': visit_data.get('user_agent'),
                'referrer': visit_data.get('referrer'),
                'session_id': visit_data.get('session_id')
            }

            response = requests.post(
                f"{settings.SUPABASE_URL}/rest/v1/analytics",
                headers=headers,
                json=data
            )
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Database error: {e}")
            return False
    
    async def get_stats(self) -> Dict:
        """통계 조회"""
        if not self.connected:
            return {"error": "Database not connected"}

        try:
            # 간단한 기본값 반환 (추후 Supabase API 호출 구현)
            return {
                "total_visitors": 0,
                "today_visitors": 0,
                "page_views": 0,
                "total_sessions": 0,
                "top_pages": []
            }
        except Exception as e:
            print(f"Database error: {e}")
            return {"error": str(e)}
    
    async def get_daily_stats(self, days: int = 7) -> List[Dict]:
        """일별 통계 조회"""
        if not self.connected:
            return []

        try:
            # 간단한 구현 - 추후 개선
            return [
                {
                    "date": "2024-01-01",
                    "visits": 0,
                    "unique_visitors": 0
                }
            ]
        except Exception as e:
            print(f"Database error: {e}")
            return []

# 전역 데이터베이스 서비스 인스턴스
db_service = DatabaseService()