#!/bin/bash
# Get all servers to listen on all ports as ECMP hashing
# can go to any of these servers depending on the state
# of the network at the time

iperf3 -sB 172.16.1.1 -p 5000 -D
iperf3 -sB 172.16.1.1 -p 5001 -D
iperf3 -sB 172.16.1.1 -p 5002 -D
iperf3 -sB 172.16.1.1 -p 5003 -D
iperf3 -sB 172.16.1.1 -p 5004 -D
iperf3 -sB 172.16.1.1 -p 5005 -D
iperf3 -sB 172.16.1.1 -p 5006 -D
iperf3 -sB 172.16.1.1 -p 5007 -D
iperf3 -sB 172.16.1.1 -p 5008 -D
iperf3 -sB 172.16.1.1 -p 5009 -D