#!/bin/bash
set -o allexport

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..

if [ -e .env ]; then
	source .env
fi
echo $HELLOSERVICE_DOCKER_IMAGE_LOCAL

docker build -t $HELLOSERVICE_DOCKER_IMAGE_LOCAL:$HELLOSERVICE_IMAGE_VERSION . 
