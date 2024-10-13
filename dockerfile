# 기본 이미지
FROM python:3.9-slim

# 필수 패키지 및 MySQL 클라이언트 설치
RUN apt-get update && \
    apt-get install -y default-mysql-client

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "app.py"]
