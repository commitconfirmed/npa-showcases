#!/bin/bash
#
# Quick script to tcpdump a Containerlab Network Device

usage="Usage: $(basename "$0") device interface \n 
EOS example - ./$(basename "$0") clab-ceos-ospf-ceos-r1 eth1"

if [[ -z $1 && -z $2 ]]; then
  echo $usage
else
  echo Running Capture on router $1 interface $2
  sudo ip netns exec $1 tcpdump -nni $2
  # Uncomment if you're running locally on Windows and want to use Wireshark
  #sudo ip netns exec $1 tcpdump -U -nni $2 -w - | /mnt/c/Program\ Files/Wireshark/wireshark.exe -k -i -
fi