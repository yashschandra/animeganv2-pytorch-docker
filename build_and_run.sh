#!/bin/bash

RUN_TYPE="$1"

IMAGE_NAME=""
if [ "$RUN_TYPE" = "lambda" ]; then
    IMAGE_NAME="animegan-pytorch-lambda"
elif [ "$RUN_TYPE" = "server" ]; then
    IMAGE_NAME="animegan-pytorch-server"
else
    echo "invalid param"
    exit 1
fi

cd $RUN_TYPE
docker build -t "$IMAGE_NAME" .
docker run -p 9000:8080 "$IMAGE_NAME"