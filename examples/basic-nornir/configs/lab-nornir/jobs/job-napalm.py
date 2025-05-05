#!/usr/bin/env python3
# Basic Nornir script to demonstrate the use of NAPALM to get device facts
# Note: Nokia SR OS devices are not supported by NAPALM it seems (not sure how to load the community plugin)
# https://napalm.readthedocs.io/en/latest/support/index.html

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_napalm.plugins.tasks import napalm_configure
from nornir.core.filter import F

def main():
    nr = InitNornir(config_file="/app/config.yml")
    filter = nr.filter(F(platform="junos") | F(platform="eos"))
    filter_junos = nr.filter(F(platform="junos"))
    filter_eos = nr.filter(F(platform="eos"))
    # Get example
    # Facts doesn't work on crpd:
    # jnpr.junos.exception.RpcError: RpcError(severity: error, bad_element: None, message: command is not valid on the crpd)
    result = filter.run(
        task=napalm_get,
        getters=["config"],
    )
    print_result(result)
    # CLI example
    result = filter.run(
        task=napalm_cli,
        commands=["show version"],
    )
    print_result(result)
    # Configuration example - Juniper
    for host in filter_junos.inventory.hosts.keys():
        print(f"Host: {host}")
        junos_config = f"set system host-name {host}-test"
        print(f"Junos config: {junos_config}")
        result = filter_junos.run(
            task=napalm_configure,
            configuration=junos_config,
        )
        print_result(result)
    # Configuration example - Arista
    for host in filter_eos.inventory.hosts.keys():
        print(f"Host: {host}")
        eos_config = f"hostname {host}-test"
        print(f"EOS config: {eos_config}")
        result = filter_eos.run(
            task=napalm_configure,
            configuration=eos_config,
        )
        print_result(result)

if __name__ == "__main__":
    main()
