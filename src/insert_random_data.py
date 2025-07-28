import random
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision

# InfluxDB connection settings
url = "http://localhost:8086"
token = "TUIki1UCLE-S282uDbxhJxGU06mREE8NMi7sQQvX9w_wvuO_MzmdyLKBF8JVt-6yvg0tjyq1d2AZueXEHvOO4Q=="
org = "TEST"
bucket = "TEST"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api()

measurement = "random_measurement"

for _ in range(100):
    value = random.uniform(0, 100)
    point = Point(measurement).field("value", value).time(datetime.utcnow(), WritePrecision.MS)
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Inserted value: {value}")
    time.sleep(0.1)

client.close()
