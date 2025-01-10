#!/bin/bash
sudo containerlab destroy -t ./basic-netbox.clab.yml
sudo docker compose --project-directory ../../composers/as-netbox/ down -v