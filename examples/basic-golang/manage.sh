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
        ./build.sh lab-golang
        cd $current_dir
        echo "Note: This lab may need the Nokia, Arista & Juniper container NOS images to be built manually!"
        ;;
        run)
        echo "Running the lab"
        sudo containerlab deploy -t ./lab.clab.yml
        echo "Done. Sleeping for 5 seconds to allow the containers to fully boot"
        sleep 5
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