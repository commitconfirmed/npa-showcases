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
        echo "Nothing to build, you will need to install cRPD manually"
        cd ../../containers/
        ./build.sh lab-ansible
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./intermediate-junos-sr.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
        sudo docker exec -tu ansible -w /app "clab-intermediate-junos-sr-lab-ansible" ansible-playbook -i inventory/inventory.yml pb-import-ssh.yml
        ;;
        cleanup)
        echo "Cleaning up the lab"
        sudo containerlab destroy -t ./intermediate-junos-sr.clab.yml
        ;;
        *)
        echo $usage
        ;;
    esac
fi