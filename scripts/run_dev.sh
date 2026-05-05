#!/bin/bash

# Set the image name
IMAGE_NAME="pythentic"
CONTAINER_NAME="pythentic"

# Build the Docker image using Podman
podman build -f dockerfile.dev -t $IMAGE_NAME .

# Check if the build was successful
if [[ $? -ne 0 ]]; then
  echo "Error: Podman build failed!"
  exit 1
fi

# Stop and remove any existing container with the same name
podman stop $CONTAINER_NAME 2>/dev/null
podman rm $CONTAINER_NAME 2>/dev/null

# Run the Docker container using Podman
podman run \
  --rm \
  -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/main.py:/app/main.py \
  -v $(pwd)/agent:/app/agent \
  -v $(pwd)/mcp_native:/app/mcp_native \
  -v $(pwd)/routes:/app/routes \
  --name $CONTAINER_NAME \
  $IMAGE_NAME

# Check if the container started successfully
if [[ $? -ne 0 ]]; then
  echo "Error: Podman run failed!"
  exit 1
fi

echo "Podman container $CONTAINER_NAME is running."
