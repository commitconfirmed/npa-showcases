## Containers

This folder contains (heh) the containers that are used in our examples and for your own deployments. Most are just pulled from the docker registry without tweaks, but some have some additions. Usually an SSH server running so your automation solution can configure it and some additional troubleshooting tools installed.

### Container Usage

These containers should all be built for you when you run the initial setup.sh script. If you want to make some manual tweaks or build an image again then just use the [build.sh](./build.sh) script.

Some additional information about each container is below:

- [GoBGP](#gobgp)

### Ansible (lab-ansible)

A container with Ansible and SSH installed

### GoBGP (lab-gobgp)

A container with GoBGP installed

### Golang (lab-godor)

A container with Golang and SSH installed

### GoBGP (lab-nornir)

A container with Nornir and SSH installed 



