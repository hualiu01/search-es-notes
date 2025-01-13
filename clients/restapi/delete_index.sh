#!/bin/bash

# Load and export variables from .env
export $(grep -v '^#' .env | xargs)

curl -u elastic:$ES_PASSWORD \
  -XDELETE $ES_ENDPOINT/shakespeare \