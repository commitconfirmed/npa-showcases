#!/usr/bin/env python3

from nornir import InitNornir

nr = InitNornir(config_file="/app/config.yml")

print("Nornir Inventory")
print(f"Hosts: {nr.inventory.hosts}")
print(f"Groups: {nr.inventory.groups}")
print(f"Defaults: {nr.inventory.defaults}")