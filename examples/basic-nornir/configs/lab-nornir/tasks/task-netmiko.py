#!/usr/bin/env python3
# Basic Nornir script to demonstrate the use of Netmiko to interact with network devices.
# Note: Nokia SR OS devices are not supported by Netmiko it seems

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_commit
from nornir_netmiko.tasks import netmiko_file_transfer
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
        task=netmiko_send_config,
        config_commands=rendered_template.split("\n"),
        enable=True,
    )
    if task.host.platform == "junos":
        task.run(
            task=netmiko_commit,
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
    
    # File transfer example
    # Note: Doesn't work on my setup
    # ValueError: Invalid output from MD5 command: /usr/libexec/ui/md5: invalid option -- 'X'
    # result = filter_junos.run(
    #     task=netmiko_file_transfer,
    #     source_file="/app/tasks/testfile",
    #     dest_file="testfile",
    # )
    # print_result(result)

    # CLI example
    result = filter.run(
        task=netmiko_send_command,
        command_string="show version",
    )
    print_result(result)
    
    # Configuration example
    result = filter.run(
        task=configure_device,
    )
    print_result(result)

if __name__ == "__main__":
    main()
