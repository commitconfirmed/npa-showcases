#!/bin/bash
#
# Basic clab management script
usage="Usage: $(basename "$0") [build|run|stop] \n 
Example to run this lab - ./$(basename "$0") run"
if [[ -z $1 ]]; then
  echo $usage
else
    current_dir=$(pwd)
    case $1 in
        build)
        cd ../../containers/
        ./build.sh lab-nornir
        ./build.sh lab-ansible
        echo "Done building containers. Building the netbox server components"
        sudo docker compose -f ../composers/lab-netbox/docker-compose.yml pull
        cd $current_dir
        echo "Done"
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./lab.clab.yml
        echo "Composing the netbox server components (this will take a few minutes)"
        echo "You can follow the progress by running 'sudo docker compose -f ../../composers/as-netbox/docker-compose.yml logs -f'"
        sudo docker compose --project-directory ../../composers/lab-netbox/ up -d
        echo "Sleeping for 30 seconds and then running compose again as this fails sometimes"
        sleep 30
        sudo docker compose --project-directory ../../composers/lab-netbox/ up -d
        echo "Done composing the netbox server components"
        ;;
        stop)
        echo "Stopping & cleaning up the lab"
        sudo containerlab destroy -t ./lab.clab.yml
        sudo docker compose --project-directory ../../composers/lab-netbox/ down -v
        ;;
        *)
        echo $usage
        ;;
    esac
fi