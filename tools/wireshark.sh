#!/bin/bash
#
# Quick script to tcpdump a Containerlab Network Device and display the output in Wireshark

usage="Usage: $(basename "$0") device interface \n 
EOS example - ./$(basename "$0") clab-lab-leaf1 eth1"

if [[ -z $1 && -z $2 ]]; then
  echo $usage
else
  echo Running Capture on router $1 interface $2
  sudo ip netns exec $1 tcpdump -U -nni $2 -w - | /mnt/c/Program\ Files/Wireshark/wireshark.exe -k -i -
fi