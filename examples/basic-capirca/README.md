# Basic Capirca

A lab showing how to generate ACLs for devices using [Capirca](https://github.com/google/capirca), and some Ansible playbook examples to generate, deploy and validate a basic ACL to an Arista and Juniper device.

Concepts: Capirca, Ansible, Config Generation, Security, ACLs, Network Automation

- [Setup](#setup)
  - [Scripts](#scripts)
- [Walkthrough](#walkthrough)

> Note: This lab uses the Arista & Juniper container NOS images. See https://github.com/commitconfirmed/npa-showcases?tab=readme-ov-file#nos-images for the steps if you haven't already installed them. 

## Setup

### Scripts

- Run `manage.sh build` to build the relevant container(s) (not needed if you have run `setup.sh`)
- Run `manage.sh run` to run the lab
- Run `manage.sh stop` to destroy the lab or simply execute `sudo containerlab destroy -t ./lab.clab.yml`

## Walkthrough

TBD