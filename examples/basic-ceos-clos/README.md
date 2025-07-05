# Basic cEOS CLOS

A lab with: 
- A basic 2 Spine and 4 Leaf setup using unnumbered BGP with IPv6 LLAs
- EVPN-VXLAN Overlay/Underlay
- Two hosts with LACP configured under a Tenant

Concepts: VXLAN, EVPN, BGP Unnumbered, Arista, EOS, Leaf, Spine, MLAG, ECMP

- [Setup](#setup)
  - [Scripts](#scripts)
- [Walkthrough](#walkthrough)

> Note: This lab uses the Arista container NOS image. See https://github.com/commitconfirmed/npa-showcases?tab=readme-ov-file#nos-images for the steps if you haven't already installed them. 

## Setup

### Scripts

- Run `manage.sh build` to build the relevant container(s) (not needed if you have run `setup.sh`)
- Run `manage.sh run` to run the lab
- Run `manage.sh stop` to destroy the lab or simply execute `sudo containerlab destroy -t ./lab.clab.yml`

## Walkthrough

TBD