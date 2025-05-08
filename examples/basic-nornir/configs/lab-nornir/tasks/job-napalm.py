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
from nornir.core.helpers.jinja_helper import render_from_file
from nornir.core.helpers.jinja_helper import render_from_string
from nornir.core.filter import F

def configure_device(task: Task) -> Result:
    #template = "set system host-name {{ task.host }}-test"
    #rendered_template = render_from_string(template, task=task)
    file = f"{task.host}.j2"
    rendered_template = render_from_file(
        template=file,
        path="/app/templates/",
        task=task)
    task.run(
        task=napalm_configure,
        configuration=rendered_template,
    )
    return Result(
        host=task.host,
        result=f"Configured {task.host.name} with template: {file}",
    )

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
    # Configuration example
    result = filter.run(
        task=configure_device,
    )
    print_result(result)

if __name__ == "__main__":
    main()
