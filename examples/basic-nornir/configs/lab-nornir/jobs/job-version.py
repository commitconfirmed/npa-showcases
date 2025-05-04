#!/usr/bin/env python3

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )

def main():
    nr = InitNornir(config_file="/app/config.yml")
    result = nr.run(task=hello_world)
    print_result(result)
    result = nr.run(
        task=napalm_get,
        getters=["facts"],
    )
    print_result(result)


if __name__ == "__main__":
    main()
