#!/bin/bash
sudo containerlab deploy -t ./basic-netbox.clab.yml
echo "Sleeping for 5 seconds to allow the containers to boot"
sleep 5
echo "Composing the netbox server components (this will take a few minutes)"
echo "You can follow the progress by running 'sudo docker compose -f ../../composers/as-netbox/docker-compose.yml logs -f'"
sudo docker compose --project-directory ../../composers/as-netbox/ up -d
echo "Sleeping for 30 seconds and then running compose again as this fails sometimes"
sleep 30
sudo docker compose --project-directory ../../composers/as-netbox/ up -d
echo "Done composing the netbox server components"