# Images

Put any images/files/etc. in here that you upload into your codespaces VM or your local install that you want ignored. i.e. the Arista cEOS image, Cisco IOL image, Juniper cRPD image, etc.

If using your own .gitignore file make sure you ignore this folders contents!

```bash
# Copyright files / images that you don't want to share
# i.e. the Arista cEOS docker image
images/**
!images/README.md
```