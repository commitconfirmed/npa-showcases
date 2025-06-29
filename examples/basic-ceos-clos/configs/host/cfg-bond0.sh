#!/bin/bash
#
# Basic script to build a 802.3ad LACP bonded interface on the host
# and configure a sub-interface with the specified VLAN ID.

usage="Usage: $(basename "$0") vlan_id \n 
Example - ./$(basename "$0") 100"

if [[ -z $1 ]]; then
  echo $usage
else
  sudo ip link add bond0 type bond
  sudo ip link set bond0 type bond mode 802.3ad lacp_active on lacp_rate fast
  sudo ip link set eth1 down
  sudo ip link set eth2 down
  sudo ip link set eth1 master bond0
  sudo ip link set eth2 master bond0
  sudo ip link add link bond0 name bond0.$1 type vlan id $1
  sudo ip link set bond0 up
fi
