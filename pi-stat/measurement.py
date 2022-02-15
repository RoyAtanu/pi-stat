import json
import util

def get_temperature():
    fields = {}
    fields['cputemp'] = util.check_CPU_temp()
    fields['gputemp'] = util.check_GPU_temp()
    return fields

def get_cpu():
    fields = {}
    cpused = util.check_CPU_used()
    core = 1
    for utilization in cpused:
        fields['cpu ' + str(core)] = utilization
        core += 1
    return fields

def get_ram():
    fields = {}
    fields['ramused'] = util.check_RAM_used()
    return fields
