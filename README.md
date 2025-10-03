# 🚀 Eojin Portfolio Backend

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11.9-3776AB?style=flat&logo=python)](https://www.python.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.15.0-499848?style=flat)](https://www.uvicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=flat&logo=postgresql)](https://supabase.com/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat&logo=render)](https://render.com/)

**김어진 포트폴리오**의 확장 가능한 백엔드 API 서버입니다. FastAPI를 기반으로 실시간 분석, 고성능 캐싱, 이벤트 기반 아키텍처를 제공합니다.

🔗 **API Docs**: [https://api.eojin.me/docs](https://api.eojin.me/docs)  
🌐 **Frontend Repository**: [eojin-portfolio](https://github.com/eojin16/eojin-portfolio)  
🎯 **Live Demo**: [https://eojin.me](https://eojin.me/)

---

## 📋 목차

- [프로젝트 개요](#-프로젝트-개요)
- [아키텍처](#-아키텍처)
- [주요 기능](#-주요-기능)
- [기술 스택](#-기술-스택)
- [프로젝트 구조](#-프로젝트-구조)
- [시작하기](#-시작하기)
- [API 엔드포인트](#-api-엔드포인트)
- [환경 변수](#-환경-변수)
- [배포](#-배포)
- [개발 로드맵](#-개발-로드맵)

---

## 🎯 프로젝트 개요

이 프로젝트는 포트폴리오 웹사이트를 위한 **확장 가능하고 성능 최적화된 백엔드 API 서버**입니다. RESTful API 설계 원칙을 따르며, 현대적인 비동기 프레임워크를 활용하여 높은 처리량과 낮은 지연 시간을 제공합니다.

### 프로젝트의 특징

- ⚡ **고성능 비동기 API**: FastAPI와 Uvicorn을 활용한 비동기 처리
- 📊 **실시간 데이터 분석**: 방문자 추적 및 통계 분석 시스템
- 🔒 **안전한 데이터 관리**: PostgreSQL(Supabase) 기반 데이터 저장
- 🚀 **자동 배포**: Render를 통한 CI/CD 파이프라인
- 📚 **자동 API 문서화**: OpenAPI(Swagger) 및 ReDoc 지원
- 🌐 **CORS 지원**: 프론트엔드와의 안전한 통신

---

## 🏗️ 아키텍처

이 백엔드는 **마이크로서비스 지향 아키텍처**를 기반으로 설계되었습니다.

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                    │
│                  https://eojin.me                        │
└──────────────────────┬──────────────────────────────────┘
                       │ REST API
                       ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend (Python)                    │
│                 api.eojin.me                             │
├──────────────────────┬──────────────────────────────────┤
│   API Layer          │   Core Layer                      │
│  ├─ analytics.py     │  ├─ config.py                     │
│  └─ routes           │  ├─ database.py                   │
│                      │  └─ security.py                   │
├──────────────────────┼──────────────────────────────────┤
│   Service Layer      │   Models Layer                    │
│  ├─ analytics        │  ├─ schemas                       │
│  ├─ cache            │  └─ database models               │
│  └─ notification     │                                   │
└──────────────────────┴──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                Infrastructure Layer                      │
├──────────────────────┬──────────────────────────────────┤
│  PostgreSQL          │  Redis Cache                      │
│  (Supabase)          │  (미래 구현)                       │
├──────────────────────┼──────────────────────────────────┤
│  Kafka               │  Monitoring                       │
│  (미래 구현)          │  (미래 구현)                       │
└─────────────────────────────────────────────────────────┘
```

### 설계 원칙

1. **계층화된 아키텍처**: API, 서비스, 데이터 계층의 명확한 분리
2. **관심사의 분리**: 각 모듈은 단일 책임 원칙을 따름
3. **확장성**: 새로운 기능 추가 시 기존 코드 영향 최소화
4. **테스트 용이성**: 의존성 주입을 통한 단위 테스트 지원

---

## ✨ 주요 기능

### 1. 실시간 방문자 분석 API

- **엔드포인트**: `/api/analytics`
- **기능**:
  - 방문자 추적 및 기록
  - 실시간 통계 데이터 제공
  - 일별/주별/월별 집계
  - 세션 분석

### 2. 고성능 데이터 처리

- 비동기 데이터베이스 커넥션 풀링
- 효율적인 쿼리 최적화
- 페이지네이션 지원

### 3. 자동 API 문서화

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- 인터랙티브한 API 테스트 환경

### 4. 캐싱 시스템 (계획 중)

- Redis 기반 캐시 레이어
- 응답 시간 최적화
- 데이터베이스 부하 감소

### 5. 이벤트 기반 아키텍처 (계획 중)

- Kafka 메시지 큐 통합
- 비동기 이벤트 처리
- 마이크로서비스 간 통신

---

## 🛠 기술 스택

### Core Framework

| 기술 | 버전 | 용도 |
|------|------|------|
| **FastAPI** | 0.68.0 | 웹 프레임워크 |
| **Uvicorn** | 0.15.0 | ASGI 서버 |
| **Python** | 3.11.9 | 프로그래밍 언어 |

### Database & Storage

| 기술 | 상태 | 용도 |
|------|------|------|
| **PostgreSQL** | ✅ 운영 중 | 주 데이터베이스 (Supabase) |
| **Redis** | 🔄 계획 중 | 캐싱, 세션 관리 |

### Message Queue & Events

| 기술 | 상태 | 용도 |
|------|------|------|
| **Kafka** | 🔄 계획 중 | 이벤트 스트리밍 |

### Utilities

| 라이브러리 | 버전 | 용도 |
|-----------|------|------|
| **python-dotenv** | 0.19.0 | 환경 변수 관리 |
| **python-multipart** | 0.0.5 | 파일 업로드 지원 |
| **httpx** | 0.23.0 | HTTP 클라이언트 |
| **requests** | 2.28.1 | HTTP 요청 |

### DevOps & Deployment

- **Render**: 클라우드 호스팅 플랫폼
- **Git**: 버전 관리
- **GitHub Actions**: CI/CD (미래 구현)

---

## 📁 프로젝트 구조

```
eojin-portfolio-backend/
├── app/                        # 애플리케이션 루트
│   ├── api/                    # API 엔드포인트
│   │   ├── __init__.py
│   │   └── analytics.py        # 분석 API
│   ├── core/                   # 핵심 설정
│   │   ├── __init__.py
│   │   ├── config.py           # 환경 설정
│   │   ├── database.py         # DB 연결 관리
│   │   └── security.py         # 인증/보안
│   ├── models/                 # 데이터 모델
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic 스키마
│   ├── services/               # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── analytics.py        # 분석 서비스
│   │   └── cache.py            # 캐시 서비스
│   ├── __init__.py
│   └── main.py                 # 애플리케이션 엔트리포인트
├── .env                        # 환경 변수 (로컬)
├── .gitignore                  # Git 제외 파일
├── README.md                   # 프로젝트 문서
├── render.yaml                 # Render 배포 설정
└── requirements.txt            # Python 의존성
```

### 주요 파일 설명

#### `app/main.py`
FastAPI 애플리케이션의 메인 엔트리포인트입니다.
- CORS 미들웨어 설정
- 라우터 등록
- 애플리케이션 이벤트 핸들러

#### `app/api/analytics.py`
방문자 분석 관련 API 엔드포인트를 정의합니다.
- `POST /analytics`: 방문 기록 추가
- `GET /analytics/stats`: 통계 조회

#### `app/core/database.py`
데이터베이스 연결 및 세션 관리를 담당합니다.
- 비동기 데이터베이스 연결 풀
- 의존성 주입을 위한 세션 생성기

---

## 🚀 시작하기

### 필요 조건

- **Python**: 3.11 이상
- **pip**: 최신 버전
- **PostgreSQL**: Supabase 계정 또는 로컬 PostgreSQL 서버

### 로컬 개발 환경 설정

1. **저장소 클론**

```bash
git clone https://github.com/eojin16/eojin-portfolio-backend.git
cd eojin-portfolio-backend
```

2. **가상 환경 생성 및 활성화**

```bash
# 가상 환경 생성
python -m venv venv

# 활성화 (Windows)
venv\Scripts\activate

# 활성화 (macOS/Linux)
source venv/bin/activate
```

3. **의존성 설치**

```bash
pip install -r requirements.txt
```

4. **환경 변수 설정**

`.env` 파일을 생성하고 다음 내용을 추가하세요:

```env
# Database
DATABASE_URL=postgresql://user:password@host:port/database
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# API
API_V1_PREFIX=/api
PROJECT_NAME=Eojin Portfolio Backend
DEBUG=True

# CORS
ALLOWED_ORIGINS=http://localhost:3000,https://eojin.me
```

5. **개발 서버 실행**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

6. **API 문서 확인**

브라우저에서 다음 URL을 열어 API 문서를 확인하세요:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌐 API 엔드포인트

### Health Check

```http
GET /
```

서버 상태를 확인합니다.

**응답 예시:**
```json
{
  "status": "healthy",
  "message": "Eojin Portfolio Backend API is running"
}
```

### Analytics API

#### 방문 기록 추가

```http
POST /api/analytics
Content-Type: application/json

{
  "page": "/",
  "sessionId": "uuid-string",
  "userAgent": "Mozilla/5.0...",
  "timestamp": "2025-09-15T10:30:00Z"
}
```

**응답:**
```json
{
  "success": true,
  "message": "Visit recorded successfully"
}
```

#### 통계 조회

```http
GET /api/analytics/stats
```

**응답:**
```json
{
  "totalVisits": 1234,
  "dailyStats": [
    {
      "date": "2025-09-15",
      "visits": 45,
      "uniqueVisitors": 32
    }
  ],
  "topPages": [
    {
      "page": "/",
      "visits": 523
    }
  ]
}
```

---

## 🔐 환경 변수

| 변수명 | 설명 | 필수 | 기본값 |
|--------|------|------|--------|
| `DATABASE_URL` | PostgreSQL 연결 문자열 | ✅ | - |
| `SUPABASE_URL` | Supabase 프로젝트 URL | ✅ | - |
| `SUPABASE_KEY` | Supabase API 키 | ✅ | - |
| `API_V1_PREFIX` | API 버전 프리픽스 | ❌ | `/api` |
| `PROJECT_NAME` | 프로젝트 이름 | ❌ | `Eojin Portfolio Backend` |
| `DEBUG` | 디버그 모드 | ❌ | `False` |
| `ALLOWED_ORIGINS` | CORS 허용 도메인 | ✅ | - |
| `REDIS_URL` | Redis 연결 URL (미래) | ❌ | - |
| `KAFKA_BROKERS` | Kafka 브로커 목록 (미래) | ❌ | - |

---

## 🚢 배포

이 프로젝트는 **Render**를 사용하여 자동 배포됩니다.

### Render 배포 프로세스

1. **GitHub 연동**: 저장소를 Render에 연결
2. **환경 변수 설정**: Render 대시보드에서 환경 변수 구성
3. **자동 배포**: `main` 브랜치에 푸시 시 자동 배포

### render.yaml 설정

```yaml
services:
  - type: web
    name: eojin-portfolio-backend
    env: python
    runtime: python-3.11.9
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### 배포 단계

1. Render 대시보드에서 새 Web Service 생성
2. GitHub 저장소 연결
3. 환경 변수 설정
4. Deploy 클릭

배포 완료 후 Render가 제공하는 URL을 통해 API에 접근할 수 있습니다.

---

## 🗺️ 개발 로드맵

### ✅ 완료된 기능 (v0.1.0 - v0.2.0)

- [x] FastAPI 기본 설정
- [x] Analytics API 구현
- [x] Supabase PostgreSQL 연동
- [x] Render 배포 설정
- [x] CORS 설정
- [x] 자동 API 문서화

### 🔄 진행 중 (v0.3.0)

- [ ] Redis 캐싱 시스템
- [ ] 인증/인가 시스템 (JWT)
- [ ] Rate Limiting
- [ ] API 버전 관리

### 📋 계획 중 (v0.4.0+)

- [ ] Kafka 메시지 큐 통합
- [ ] 실시간 모니터링 대시보드
- [ ] 로깅 및 에러 트래킹 (Sentry)
- [ ] API 테스트 자동화
- [ ] CI/CD 파이프라인 (GitHub Actions)
- [ ] Docker 컨테이너화
- [ ] Kubernetes 오케스트레이션

---

## 📈 개발 히스토리

### v0.1.0 (2025년 9월 15일)
- ✅ 프로젝트 초기 설정
- ✅ FastAPI 백엔드 구조 설계
- ✅ Analytics API 기본 구현

### v0.2.0 (2025년 9월 16일)
- ✅ 데이터베이스 연결 리팩토링
- ✅ Render 배포 설정 추가
- ✅ 환경 변수 관리 개선
- ✅ 의존성 업데이트

---

## 📄 라이선스

이 프로젝트는 개인 포트폴리오 목적으로 제작되었습니다.

---

## 🔗 연관 프로젝트

- **Frontend**: [eojin-portfolio](https://github.com/eojin16/eojin-portfolio)
- **Live Site**: [https://eojin.me](https://eojin.me)

---

## 📞 연락처

프로젝트 관련 문의사항이 있으시면 GitHub Issues를 통해 연락주세요.

**GitHub**: [@eojin16](https://github.com/eojin16)

---

## 🙏 감사의 글

- [FastAPI](https://fastapi.tiangolo.com/) - 웹 프레임워크
- [Render](https://render.com/) - 배포 플랫폼
- [Supabase](https://supabase.com/) - PostgreSQL 호스팅
- [Uvicorn](https://www.uvicorn.org/) - ASGI 서버

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/eojin16">eojin16</a>
</p>

<p align="center">
  <sub>Last Updated: September 2025</sub>
