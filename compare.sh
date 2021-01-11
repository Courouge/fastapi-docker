#!/usr/bin/env bash

#tag1="python3-alpine__gcr.io/distroless/python3-debian10"
tag1="alpine_distroless"
#tag2="python3-slim__gcr.io/distroless/python3-debian10"
tag2="slim_distroless"


#docker build -t "$tag1" --file "${tag1}/Dockerfile" -q "./${tag1}/"  && docker image ls |grep "$tag1" && docker run -p 8000:8000 -it "$tag1"
docker build -t "$tag2" --file "${tag2}/Dockerfile" -q "./${tag2}/" && docker image ls |grep "$tag2" && docker run -p 8000:8000 -it "$tag2"

#docker build -t "$use_tag" --file "./docker-images/${DOCKERFILE}.dockerfile" "./docker-images/"