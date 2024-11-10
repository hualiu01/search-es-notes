On computer restart, what described in `0_local_installation_steps.md` failed. 

Thus, Here we will have a docker-compose to have the env ready every time.

# (Optional) remove all running containers and images
```
docker container rm -f $(docker container ls -aq)
```
- `-f` --force     Force the removal of a running container (uses SIGKILL)
- `-a`, --all             Show all containers (default shows just running), now it also shows stopped
- `-q`, --quiet           Only display container IDs

```
docker image rm $(docker image ls -q)
```

# First time only - spin up the ES container only and set Kibana PW

spin up the ES container only
```
docker compose up -d elasticsearch
```
set Kibana PW: NO NEED TO GET A INTERACTIVE BASH. JUST RUN THIS IN ANY TERMINAL
```
./setup_kibana_pw.sh
```
Stop all containers:
```
docker container stop $(docker container ls -aq)
```

# Spin up the ES container and Kibana container together

```
docker compose up
```