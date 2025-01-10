#!/bin/bash
#
# Build the specified container. Should already be done by setup.sh
# But this script can be used to build a single container if needed.

usage="Usage: $(basename "$0") container \n 
Example to build the lab-gobgp container - ./$(basename "$0") lab-gobgp"

if [[ -z $1 ]]; then
  echo $usage
else
  cd $1
  sudo docker build -t $1 .
  if [ "$(sudo docker image list -qf dangling=true)" ]; then
    sudo docker image rm $(sudo docker image list -qf dangling=true)
  fi
fi