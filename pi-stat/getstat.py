import measurement, os, time
from datetime import datetime
from decouple import config
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

def start_monitor():
    influx_org = config('PISTAT_INFLUX_ORG')
    influx_bucket = config('PISTAT_INFLUX_BUCKET')

    client = influxdb_client.InfluxDBClient(
        url=config('PISTAT_INFLUX_URL'),
        token=config('PISTAT_INFLUX_TOKEN'),
        org=influx_org
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)

    temperature = measurement.get_temperature()
    cpu = measurement.get_cpu()
    ram = measurement.get_ram()
    network = measurement.get_network()
    json_body = [
        {
            "measurement": "temperature",
            "tags": {"source": "pi"},
            "fields": temperature
        },
        {
            "measurement": "cpu",
            "tags": {"source": "pi"},
            "fields": cpu
        },
        {
            "measurement": "ram",
            "tags": {"source": "pi"},
            "fields": ram
        },
        {
            "measurement": "network",
            "tags": {"source": "pi"},
            "fields": network
        }
    ]
    write_api.write(bucket=influx_bucket, org=influx_org, record=json_body)

    print('record inserted at : ' + str(datetime.now()))

def main():
    interval = int(config('PISTAT_INTERVAL'))
    while True:
        start_monitor()
        time.sleep(interval)

if __name__ == "__main__":
    main()