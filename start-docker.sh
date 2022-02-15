#!/bin/bash

sudo docker run -d \
      -p 8086:8086 \
      -v $PWD/data:/var/lib/influxdb2 \
      -v $PWD/config:/etc/influxdb2 \
      -e DOCKER_INFLUXDB_INIT_MODE=setup \
      -e DOCKER_INFLUXDB_INIT_USERNAME=piuser \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=pipassword \
      -e DOCKER_INFLUXDB_INIT_ORG=pi \
      -e DOCKER_INFLUXDB_INIT_BUCKET=pistat \
      -e DOCKER_INFLUXDB_INIT_RETENTION=1w \
      -e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=opensecret \
      --name=influxdb \
      influxdb:1.8

sudo docker run -d \
      -p 3000:3000 \
      --name=grafana \
      -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
      grafana/grafana-oss