from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class AnalyticsCreate(BaseModel):
    page_path: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    referrer: Optional[str] = None
    session_id: Optional[str] = None

class AnalyticsResponse(BaseModel):
    id: int
    page_path: str
    ip_address: Optional[str]
    user_agent: Optional[str]
    referrer: Optional[str]
    session_id: Optional[str]
    created_at: datetime

class StatsResponse(BaseModel):
    total_visitors: int
    today_visitors: int
    page_views: int
    total_sessions: int
    top_pages: List[dict]

class PageVisit(BaseModel):
    page: str
    count: int

class DailyStats(BaseModel):
    date: str
    visits: int
    unique_visitors: int