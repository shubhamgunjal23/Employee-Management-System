# Employee Management System

CRUD foundation and complete 3-tier AWS deployment.

## Local
docker compose up --build

Frontend: http://localhost:8080
API: http://localhost:8000/health

## AWS
CloudFront -> S3 frontend
ALB -> Target Group -> Auto Scaling EC2 Docker containers -> RDS PostgreSQL
CloudWatch -> alarms -> SNS

## Load test
k6 run -e BASE_URL=http://YOUR_ALB_DNS loadtest/k6.js
