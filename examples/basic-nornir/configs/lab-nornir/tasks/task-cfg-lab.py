#!/usr/bin/env python3
# Initial task to configure the lab devices
# At the moment it just creates an admin account on the crpd device

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_commit
from nornir.core.helpers.jinja_helper import render_from_file

# Need to configure a non-root user on crpd for the scrapli tasks to work
def create_user(task: Task) -> Result:
    configuration = [
        "set system login user admin uid 100 class super-user",
        "set system login user admin authentication encrypted-password \"$6$fqT2/$vs6BJFI4T2mHaOPQOlSdhwO2afjkF9k804FguaJ8ccKGAr.QNVThG5hHO2bycdCEaqeGCRAShfQRAk2zlOSl61\"",
    ]
    task.run(
        task=netmiko_send_config,
        config_commands=configuration,
        enable=True,
    )
    task.run(
        task=netmiko_commit,
    )
    return Result(
        host=task.host,
        result=f"Configured admin user on {task.host.name}",
    )

def main():
    nr = InitNornir(config_file="/app/config.yml")
    filter = nr.filter(platform="junos")
    # User root account to initially connect to the device
    # So we can create a non-root user
    for host in filter.inventory.hosts.values():
        host.username = "root"
        host.password = "clab123"

    # Set password
    result = filter.run(
        task=create_user,
    )
    print_result(result)

if __name__ == "__main__":
    main()
