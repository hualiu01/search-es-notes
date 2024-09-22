source: https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html 

# 1 set password
export ELASTIC_PASSWORD="<ES_PASSWORD>"  # password for "elastic" username
-  ES_PASSWORD is set to h*4 for me
export KIBANA_PASSWORD="<KIB_PASSWORD>"  # Used _internally_ by Kibana, must be at least 6 characters long
- KIB_PASSWORD is set to kibana_*4 for me

# 2 Create a Docker network
```
docker network create elastic-net
```

# 3 Run Elasticsearch local containar in "single-node" mode
```
docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch --network elastic-net \
  -e ELASTIC_PASSWORD=$ELASTIC_PASSWORD \
  -e "discovery.type=single-node" \
  -e "xpack.security.http.ssl.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.1
```
-p, --publish list                     Publish a container's port(s) to the host
    - syntax `-p HOST_PORT:CONTAINER_PORT`
-d, --detach                           Run container in background and print container ID
--name string                          Assign a name to the container
--network network                  Connect a container to a network
-e, --env list                         Set environment variables

# 4 set the kibana_system password in the Elasticsearch container
```
curl -u elastic:$ELASTIC_PASSWORD \
  -X POST \
  http://localhost:9200/_security/user/kibana_system/_password \
  -d '{"password":"'"$KIBANA_PASSWORD"'"}' \
  -H 'Content-Type: application/json'
```

# Start the Kibana container 
```
docker run -p 127.0.0.1:5601:5601 -d --name kibana --network elastic-net \
  -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
  -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 \
  -e ELASTICSEARCH_USERNAME=kibana_system \
  -e ELASTICSEARCH_PASSWORD=$KIBANA_PASSWORD \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  docker.elastic.co/kibana/kibana:8.15.1
```
__When you access Kibana, use `elastic` as the username and the password you set earlier for the ELASTIC_PASSWORD environment variable.__

# Connect from browser
You’ll use the following connection details:

Elasticsearch endpoint: http://localhost:9200
Username: elastic
Password: $ELASTIC_PASSWORD (Value you set in the environment variable)