import re, subprocess
import psutil
import time
 
def check_GPU_temp():
    temp = 0
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search('temp=(.+?)\'C', msg)
        try:
            if m:
                temp = float(m.group(1))
        except ValueError:
            pass
    return temp

def check_CPU_temp():
    temp = 0
    err, msg = subprocess.getstatusoutput('cat /sys/class/thermal/thermal_zone*/temp')
    if not err:
        temp = float(msg)/1000
    return temp

def check_CPU_used():
    return psutil.cpu_percent(percpu=True)

def check_RAM_used():
    return psutil.virtual_memory().percent

def check_SWAP_used():
    return psutil.swap_memory().percent

def check_network_io():
    io1 = psutil.net_io_counters(nowrap=True)
    time.sleep(1)
    io2 = psutil.net_io_counters(nowrap=True)
    bytesent = io2.bytes_sent - io1.bytes_sent
    bytereceived = io2.bytes_recv - io1.bytes_recv
    return bytesent, bytereceived
