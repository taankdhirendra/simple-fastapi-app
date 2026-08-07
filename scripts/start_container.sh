#!/bin/bash
set -e

IMAGE="taankdhirendra/fastapi-demo:latest"
CONTAINER="fastapi-demo"

echo "Pulling latest image..."
docker pull $IMAGE

echo "Stopping existing container..."
docker stop $CONTAINER || true

echo "Removing existing container..."
docker rm $CONTAINER || true

echo "Starting new container..."
docker run -d \
  --name $CONTAINER \
  -p 8000:8000 \
  --restart unless-stopped \
  $IMAGE

