#!/bin/bash
# We will run this manually as the network takes a while to configure and converge.
# Have to use different source IPs due to the 3-Tuple hashing on the Arista image
# Also as the iperf3 server only accepts a single TCP connection on its port at a 
# time we have to use multiple ports.

iperf3 -c 172.16.1.1 -p 5000 -b 8M -t 120s --logfile client-5000-stats.txt &
iperf3 -c 172.16.1.1 -p 5001 -b 8M -t 120s --logfile client-5001-stats.txt &
iperf3 -c 172.16.1.1 -p 5002 -b 8M -t 120s --logfile client-5002-stats.txt &
iperf3 -c 172.16.1.1 -p 5003 -b 8M -t 120s --logfile client-5003-stats.txt &
iperf3 -c 172.16.1.1 -p 5004 -b 8M -t 120s --logfile client-5004-stats.txt &
iperf3 -c 172.16.1.1 -p 5005 -b 8M -t 120s --logfile client-5005-stats.txt &
iperf3 -c 172.16.1.1 -p 5006 -b 8M -t 120s --logfile client-5006-stats.txt &
iperf3 -c 172.16.1.1 -p 5007 -b 8M -t 120s --logfile client-5007-stats.txt &
iperf3 -c 172.16.1.1 -p 5008 -b 8M -t 120s --logfile client-5008-stats.txt &
iperf3 -c 172.16.1.1 -p 5009 -b 8M -t 120s --logfile client-5009-stats.txt &