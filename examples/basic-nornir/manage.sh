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
        echo "Building relevant lab containers"
        ../../containers/build.sh lab-nornir
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./basic-nornir.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
        ;;
        cleanup)
        echo "Cleaning up the lab"
        sudo containerlab destroy -t ./basic-nornir.clab.yml
        ;;
        *)
        echo $usage
        ;;
    esac
fi