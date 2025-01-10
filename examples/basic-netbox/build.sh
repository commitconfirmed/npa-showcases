#!/bin/bash
# Build the required docker images for this lab if not already done
# Using the setup.sh script (to save time)
echo "Building containers..."
cd ../../containers/
./build.sh as-ansible
./build.sh as-bird
echo "Done building containers"
echo "Building the netbox server components"
# Only one ../ needed as we are in the containers directory already
sudo docker compose -f ../composers/as-netbox/docker-compose.yml pull