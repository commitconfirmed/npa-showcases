#!/bin/bash
# Add multiple IP's to eth1 to better use the 3-tuple 
# ECMP hashing available on the cEOS container

ip addr add 172.16.10.100/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.101/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.102/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.103/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.104/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.105/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.106/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.107/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.108/24 brd 172.16.10.255 dev eth1
ip addr add 172.16.10.109/24 brd 172.16.10.255 dev eth1