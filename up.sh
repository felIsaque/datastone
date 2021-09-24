#!/usr/bin/env bash

ENV_APP="$1"

sed -i "s/DEB.*/DEB=${ENV_APP}/" .env

docker-compose up
