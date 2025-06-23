#!/bin/bash
#
# Initial setup script for the project. This script will build the containers
# in the containers directory so they can be used by Containerlab. You can run
# this script again to rebuild the containers if you make changes to them or
# if you want to update the base images to the latest versions.

set -e
echo "Pulling latest registry images"
sudo docker pull gnmic/gnmic:latest
sudo docker pull prom/prometheus:latest
sudo docker pull grafana/grafana:main-ubuntu
sudo docker pull ubuntu:latest

echo "Building all custom containers"
for container in containers/*; do
  if [ -d "$container" ] && [ "$container" != "containers/community" ]; then
    container_name=$(basename "$container")
    echo "Building $container_name"
    sudo docker build -t $container_name ./$container/.
  fi
done

echo "Removing dangling images"
if [ "$(sudo docker image list -qf dangling=true)" ]; then
  sudo docker image rm $(sudo docker image list -qf dangling=true)
fi