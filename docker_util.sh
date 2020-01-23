#!/bin/bash

docker build -t sldsc .
docker tag sldsc gcr.io/finucane-dp5/sldsc:latest
docker push gcr.io/finucane-dp5/sldsc:latest
