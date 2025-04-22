#!/bin/bash
#
# Manage the lab
usage="Usage: $(basename "$0") [build|run|cleanup] \n 
Example to run this lab - ./$(basename "$0") run"
if [[ -z $1 ]]; then
  echo $usage
else
    case $1 in
        build)
        echo "Note: you will need to download and build cRPD manually"
        cd ../../containers/
        ./build.sh lab-ansible
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./lab.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
        sudo docker exec -tu ansible -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml pb-import-ssh.yml
        sudo docker exec -tu ansible -w /app "clab-lab-ansible" ansible-playbook -i inventory/inventory.yml playbooks/pb-cfg-lab.yml
        ;;
        cleanup)
        echo "Cleaning up the lab"
        sudo containerlab destroy -t ./lab.clab.yml
        ;;
        *)
        echo $usage
        ;;
    esac
fi