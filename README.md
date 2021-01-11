# Quickstart fastapi lightweight docker images
Based on https://github.com/tiangolo/fastapi project

First I am a big fan of fastapi framework and I hope this repo will be helpful.</br>
The goal of this repository is to provide simple lightweight fastapi images !

## alpine_distroless [52.3MB]

Based on `python:3-alpine` and `gcr.io/distroless/python3-debian10`

## slim_distroless [95.8MB]

Based on `python:3-slim` and `gcr.io/distroless/python3-debian10`

## Build container
```console
$ docker build -t small_fast_api .
```
## Run container
```console
$ docker run -p 8000:8000 -it small_fast_api
```
## Delete container
```console
$ docker kill $(docker ps -a -q)
```
`docker kill $(docker ps -a -q)`

## Oneliner
```console
$ docker kill $(docker ps -a -q) && docker build -t small_fast_api . && docker run -p 8000:8000 -it small_fast_api
```

## Contribute ;)

## Compare
./compare.sh
