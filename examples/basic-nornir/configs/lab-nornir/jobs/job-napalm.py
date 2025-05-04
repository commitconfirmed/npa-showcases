#!/usr/bin/env python3
# Basic Nornir script to demonstrate the use of NAPALM to get device facts
# Note: Nokia SR OS devices are not supported by NAPALM it seems
# https://napalm.readthedocs.io/en/latest/support/index.html

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_cli
from nornir.core.filter import F

def main():
    nr = InitNornir(config_file="/app/config.yml")
    filter = nr.filter(F(platform="junos") | F(platform="eos"))
    # Facts doesn't work on crpd either:
    # jnpr.junos.exception.RpcError: RpcError(severity: error, bad_element: None, message: command is not valid on the crpd)
    '''
    result = filter.run(
        task=napalm_get,
        getters=["facts"],
    )
    print_result(result)
    '''
    result = filter.run(
        task=napalm_cli,
        commands=["show version"],
    )
    print_result(result)


if __name__ == "__main__":
    main()
