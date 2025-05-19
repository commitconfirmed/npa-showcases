#!/usr/bin/env python3

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result as print_result_nornir
from nornir_rich.functions import print_inventory, print_result

nr = InitNornir(config_file="/app/config.yml")

# Basic task
def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )

def main():
    print("--------------------------------")
    print("Default Nornir Inventory \n--------------------------------")
    print(f"Hosts: {nr.inventory.hosts}")
    print(f"Groups: {nr.inventory.groups}")
    print(f"Specific host details (ceos1):")
    for key, value in nr.inventory.hosts["ceos1"].items():
        print(f"  {key}: {value}")
    print("--------------------------------")

    print("Nornir Inventory with Rich \n--------------------------------")
    print_inventory(nr)
    print("--------------------------------")

    result = nr.run(task=hello_world)
    print("Default Nornir task \n--------------------------------")
    print_result_nornir(result)
    print("--------------------------------")
    print("Nornir task with Rich \n--------------------------------")
    print_result(result)
    
    print("--------------------------------")
    print("Nornir task with Rich (Filtered) \n--------------------------------")
    result = nr.filter(platform="junos").run(task=hello_world)
    print_result(result)

if __name__ == "__main__":
    main()