#!/bin/bash
#
# Initial setup script for the ASNAC project. This script will build the containers
# in the containers directory so they can be used by Containerlab.

set -e
echo "Building all containers"
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