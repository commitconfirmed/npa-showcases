#!/usr/bin/env python3
# Basic Nornir script to demonstrate the use of Scrapli to interact with network devices.
# Note: Nokia SR OS devices are not supported by Scrapli it seems

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs
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
        task=send_configs,
        configs=rendered_template.split("\n"),
        eager=True,
    )
    if task.host.platform == "junos":
        task.run(
            task=send_configs,
            configs=["show | compare", "commit check", "commit"],
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

    # CLI example
    result = filter.run(
        task=send_command,
        command="show version",
    )
    print_result(result)
    
    # Configuration example
    result = filter.run(
        task=configure_device,
    )
    print_result(result)

if __name__ == "__main__":
    main()
