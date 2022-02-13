import util, os, time
from datetime import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

URL = 'http://localhost:8086'
TOKEN = 'opensecret'
ORG = 'pi'
BUCKET = 'pistat'

INTERVAL = 5


def start_monitor():
    client = influxdb_client.InfluxDBClient(
        url=URL,
        token=TOKEN,
        org=ORG
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)

    cputemp = util.check_CPU_temp()
    gputemp = util.check_GPU_temp()
    json_body = [
        {
            "measurement": "temperature",
            "tags": {
                "source": "pi"
            },
            "fields": {
                "cputemp": cputemp,
                "gputemp": gputemp
            }
        }
    ]
    write_api.write(bucket=BUCKET, org=ORG, record=json_body)

    print('record inserted at : ' + str(datetime.now()))

def main():
    while True:
        start_monitor()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()