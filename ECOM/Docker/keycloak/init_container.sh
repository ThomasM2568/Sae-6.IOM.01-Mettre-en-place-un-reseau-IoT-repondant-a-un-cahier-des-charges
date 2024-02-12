#!/bin/bash

sudo docker run --name keycloak -p 8080:8080 \
    -e KEYCLOAK_ADMIN=admin \
    -e KEYCLOAK_ADMIN_PASSWORD=admin \
    -v keycloak_save:/opt/keycloak/data \
    quay.io/keycloak/keycloak:latest start-dev
