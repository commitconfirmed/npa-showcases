#!/bin/bash
#
# Import ceos and crpd images and tag as latest

sudo docker import images/cEOS64-lab-*.tar.xz ceos:latest
sudo docker image load -i images/junos-routing-crpd-docker-amd64-*.tgz
sudo docker image tag `sudo docker image list | grep crpd | awk '{print $1 ":" $2}'` crpd:latest