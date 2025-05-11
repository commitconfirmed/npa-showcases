# Images

Put any images/files/etc. in here that you upload into your codespaces VM or your local install that you want ignored. i.e. the Arista cEOS image, Cisco IOL image, Juniper cRPD image, etc. Instructions below to add images:

```bash
❯ sudo docker image pull ghcr.io/nokia/srlinux
Using default tag: latest
--snip--
❯ sudo docker import cEOS64-lab-4.32.5.1M.tar.xz ceos:latest
sha256:70314310c219009aa903f9ce57f1eef4a72337f21dc3b778179724203c8a31f1
❯ sudo docker image load -i junos-routing-crpd-docker-amd64-23.2R1.13.tgz
Loaded image: crpd:23.2R1.13
❯ sudo docker image tag crpd:23.2R1.13 crpd:latest
```

If using your own .gitignore file make sure you ignore this folders contents!

```bash
# Copyright files / images that you don't want to share
# i.e. the Arista cEOS docker image
images/**
!images/README.md
```
