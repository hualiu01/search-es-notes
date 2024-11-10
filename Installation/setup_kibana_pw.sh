#!/bin/bash

# Load and export variables from .env
export $(grep -v '^#' .env | xargs)

echo "ELASTIC_PASSWORD=$ELASTIC_PASSWORD"
echo "KIBANA_PASSWORD=$KIBANA_PASSWORD"

# Set up Kibana sys pw in ES, authenticated as elastic user
curl -u elastic:$ELASTIC_PASSWORD \
  -X POST \
  http://localhost:9200/_security/user/kibana_system/_password \
  -d '{"password":"'"$KIBANA_PASSWORD"'"}' \
  -H 'Content-Type: application/json'