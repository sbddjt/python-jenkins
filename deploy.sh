#!/bin/bash

IMAGE_NAME="sbddjt/python-calculator"
IMAGE_TAG=$1

echo "▶ 기존 컨테이너 중지 및 삭제"
docker stop python-app 2>/dev/null || true
docker rm python-app 2>/dev/null || true

echo "▶ 최신 이미지 Pull"
docker pull ${IMAGE_NAME}:${IMAGE_TAG}

echo "▶ 새 컨테이너 실행"
docker run -d \
  --name python-app \
  --restart always \
  -p 8000:8000 \
  ${IMAGE_NAME}:${IMAGE_TAG}

echo "▶ 오래된 이미지 정리"
docker image prune -f

echo "✅ 배포 완료!"