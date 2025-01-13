#!/bin/bash

# Load and export variables from .env
export $(grep -v '^#' .env | xargs)

curl -u elastic:$ES_PASSWORD \
  -H "Content-type: application/json" \
  -XPUT $ES_ENDPOINT/shakespeare/_bulk \
  --data-binary @data/shakespeare_8.0.json