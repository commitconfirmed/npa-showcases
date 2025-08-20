# Images

Put any images/files/etc. in here that you upload into your codespaces VM or your local install that you want ignored. i.e. the Arista cEOS image, Juniper cRPD image, etc. Instructions below to add images:

```bash
❯ sudo docker image pull ghcr.io/nokia/srlinux
Using default tag: latest
--snip--
❯ sudo docker import cEOS64-lab-4.32.5.1M.tar.xz ceos:latest
sha256:70314310c219009aa903f9ce57f1eef4a72337f21dc3b778179724203c8a31f1
❯ sudo docker image load -i junos-routing-crpd-docker-amd64-23.2R1.13.tgz
Loaded image: crpd:23.2R1.13
❯ sudo docker image tag crpd:23.2R1.13 crpd:latest
❯ sudo docker load -i cJunosEvolved-25.2R1.8-EVO.tar.gz
Loaded image: cjunosevolved:25.2R1.8-EVO
❯ sudo docker image tag cjunosevolved:25.2R1.8-EVO cjunosevolved:latest
```

If using your own .gitignore file make sure you ignore this folders contents!

```bash
# Copyright files / images that you don't want to share
# i.e. the Arista cEOS docker image
images/**
!images/README.md
```

## What, no Cisco?

Unfortunately from what I can gather the Cisco IOS on Linux (IOL) image is still a VM so it doesn't really fit with the aim of this repo. Maybe a container image will be available one day for free...

If you're building this at home you can follow the links available below which "should" work with the free tier Cisco CML iso (CCO account required)

https://containerlab.dev/manual/kinds/cisco_iol/

https://developer.cisco.com/docs/modeling-labs/cml-free/

