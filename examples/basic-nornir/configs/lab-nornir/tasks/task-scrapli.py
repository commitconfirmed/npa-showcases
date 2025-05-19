#!/usr/bin/env python3
# Basic Nornir script to demonstrate the use of Scrapli to interact with network devices.
# Note: Nokia SR OS devices are not supported by Scrapli it seems

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs
from nornir_scrapli.functions import print_structured_result
from nornir.core.helpers.jinja_helper import render_from_file
from nornir.core.filter import F

def configure_device_junos(task: Task) -> Result:
    file = f"{task.host}.j2"
    rendered_template = render_from_file(
        template=file,
        path="/app/templates/",
        task=task)
    # Load the config
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
    print_structured_result(result, fail_to_string=True)
    
    # Configuration example
    result = filter_junos.run(
        task=configure_device_junos,
    )
    print_result(result)

if __name__ == "__main__":
    main()
