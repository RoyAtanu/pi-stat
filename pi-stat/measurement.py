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
    fields['swapused'] = util.check_SWAP_used()
    return fields

def get_network():
    bytesent, bytereceived = util.check_network_io()
    fields = {}
    fields['bytesent'] = bytesent
    fields['bytereceived'] = bytereceived
    return fields
