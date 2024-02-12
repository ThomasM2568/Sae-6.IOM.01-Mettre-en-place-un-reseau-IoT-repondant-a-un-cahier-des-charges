#!/bin/bash

sudo docker run --name keycloak -p 8080:8080 \
    -e KEYCLOAK_ADMIN= $1 \
    -e KEYCLOAK_ADMIN_PASSWORD= $2 \
    -v keycloak_save:/opt/keycloak/data \
    quay.io/keycloak/keycloak:latest start-dev
