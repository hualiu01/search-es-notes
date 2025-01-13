#!/bin/bash

# Load and export variables from .env
export $(grep -v '^#' .env | xargs)

curl -u elastic:$ES_PASSWORD \
  -H "Content-type: application/json" \
  -XGET $ES_ENDPOINT/shakespeare/_search?pretty \
  -d '{"query" : {"match_phrase" : {"text_entry" : "to be or not to be"}}}'