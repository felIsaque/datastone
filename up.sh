#!/usr/bin/env bash

ENV_APP="$1"

sed -i "s/DEB.*/DEB=${ENV_APP}/" .env

if [ $ENV_APP == "FALSE" ]
then
    docker-compose up
else
    docker-compose -f docker-compose.prod.yml up
fi
