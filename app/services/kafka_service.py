from kafka import KafkaProducer, KafkaConsumer
import json
import asyncio
from typing import Dict
from app.core.config import settings

class KafkaService:
    def __init__(self):
        self.producer = None
        self.consumer = None
    
    async def connect(self):
        """Kafka 연결"""
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=[settings.KAFKA_BOOTSTRAP_SERVERS],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Kafka connected")
        except Exception as e:
            print(f"⚠️  Kafka connection failed: {e}")
            self.producer = None
    
    async def disconnect(self):
        """Kafka 연결 종료"""
        if self.producer:
            self.producer.close()
    
    async def send_analytics_event(self, event_data: Dict):
        """분석 이벤트 전송"""
        if self.producer:
            try:
                self.producer.send('analytics-events', event_data)
                self.producer.flush()
            except Exception as e:
                print(f"Kafka send error: {e}")
    
    async def send_notification(self, notification_data: Dict):
        """알림 이벤트 전송"""
        if self.producer:
            try:
                self.producer.send('notifications', notification_data)
                self.producer.flush()
            except Exception as e:
                print(f"Kafka notification error: {e}")

# 전역 Kafka 서비스 인스턴스
kafka_service = KafkaService()