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
        cd $current_dir
        echo "Note: you will need to download and build cRPD manually for this lab!"
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./lab.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
        #sudo docker exec -tu ansible -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml pb-import-ssh.yml
        #sudo docker exec -tu ansible -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml playbooks/pb-cfg-lab.yml
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