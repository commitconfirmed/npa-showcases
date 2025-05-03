#!/usr/bin/env python3

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )

nr = InitNornir(config_file="/app/config.yml")
result = nr.run(task=hello_world)
print_result(result)

