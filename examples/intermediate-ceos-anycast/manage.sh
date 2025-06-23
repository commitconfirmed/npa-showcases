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
        ./build.sh lab-ansible
        ./build.sh lab-bird
        ./build.sh lab-host
        cd $current_dir
        sudo docker pull grafana/grafana:main-ubuntu
        sudo docker pull gnmic/gnmic:latest
        sudo docker pull prom/prometheus:latest
        sudo docker pull grafana/grafana:main-ubuntu
        echo "Note: you will need to download and build cEOS manually for this lab!"
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./lab.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
        sudo docker exec -tu admin -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml pb-import-ssh.yml
        sudo docker exec -tu admin -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml pb-cfg-lab.yml
        ;;
        stop)
        echo "Stopping & cleaning up the lab"
        sudo containerlab destroy -t ./lab.clab.yml
        ;;
        *)
        echo $usage
        ;;
    esac
fi