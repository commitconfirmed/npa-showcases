# Basic Netbox

A lab going over the basics of netbox and some basic ways you can interact with it to import data and how you can hook Ansible & Nornir into it.

> **Note**: Due to the nature/conflict of docker compose and containerlab, the Netbox server cannot have a static IP set in the Containerlab management network. Luckily compose will add a dns entry under netbox for us

- [Basic Netbox](#basic-netbox)
  - [Setup](#setup)
    - [Script](#script)
    - [Manually](#manually)
  - [Walkthrough](#walkthrough)

## Setup

### Script

- Run the build.sh script to build the relevant containers and perform a docker compose pull on the netbox composer
- Run the run.sh script to build the containerlab and bring up the netbox composer

You may see the below error on the first runthrough if using codespaces:

netbox-1               |   Applying taggit.0005_auto_20220424_2025... OK
netbox-1               |   Applying taggit.0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx... OK
dependency failed to start: container as-netbox-netbox-1 is unhealthy

Simply wait a few minutes and then run docker compose up again

### Manually

TBD

## Walkthrough

Importing:

- HTTP GUI
- Postman
- CSV
- Ansible
- Python Script
