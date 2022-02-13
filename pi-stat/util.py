import re, subprocess
 
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
