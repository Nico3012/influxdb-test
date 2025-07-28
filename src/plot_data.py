import argparse
from influxdb_client import InfluxDBClient
import matplotlib.pyplot as plt
from datetime import datetime

# InfluxDB connection settings
url = "http://localhost:8086"
token = "K2gLIVr56Rg8TygeYikSBCKYJFiD0GayeYt7QKGdPR-uzXuy1YeYCDEbStbyR9MbNqXq-2ZLw5WAe_2Xig3sNg=="  # Must match DOCKER_INFLUXDB_INIT_PASSWORD
org = "TEST"                    # Must match DOCKER_INFLUXDB_INIT_ORG
bucket = "TEST"                 # Must match DOCKER_INFLUXDB_INIT_BUCKET

parser = argparse.ArgumentParser(description="Plot data from InfluxDB for a given time interval.")
parser.add_argument('--start', required=True, help='Start time (RFC3339 format, e.g. 2025-07-28T00:00:00Z)')
parser.add_argument('--stop', required=True, help='Stop time (RFC3339 format, e.g. 2025-07-28T23:59:59Z)')
args = parser.parse_args()

client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

query = f'''
from(bucket: "{bucket}")
  |> range(start: {args.start}, stop: {args.stop})
  |> filter(fn: (r) => r["_measurement"] == "random_measurement")
  |> filter(fn: (r) => r["_field"] == "value")
'''

result = query_api.query(org=org, query=query)
times = []
values = []
for table in result:
    for record in table.records:
        times.append(record.get_time())
        values.append(record.get_value())

plt.plot(times, values, marker='o')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Random Data from InfluxDB')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

client.close()
