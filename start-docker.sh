#!/bin/bash

# if you don't have docker-compose installed, use this script to run influxdb ang grafana docker containers

sudo docker run -d \
      -p 8086:8086 \
      -v $PWD/data:/var/lib/influxdb2 \
      -v $PWD/config:/etc/influxdb2 \
      -e INFLUXDB_ADMIN_USER=piuser \
      -e INFLUXDB_ADMIN_PASSWORD=pipassword \
      -e INFLUXDB_DB=pistat \
      --name=influxdb \
      influxdb:1.8

sudo docker run -d \
      -p 3000:3000 \
      --name=grafana \
      -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
      grafana/grafana-oss