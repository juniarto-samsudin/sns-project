import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "IHPC"
url = "http://192.168.1.15:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="sample-bucket"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
""" for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="IHPC", record=point)
  time.sleep(1) # separate points by 1 second """

""" for value in range(5):
  point = (
    Point("home")
    .tag("room", "kitchen")
    .field("temp", value)
  )
  write_api.write(bucket=bucket, org="IHPC", record=point)
  time.sleep(1) # separate points by 1 second """

#from(bucket: "sample-bucket")
#  |> range(start: -1h)

""" query_api = write_client.query_api()
query = f'from(bucket: "sample-bucket") |> range(start: -1h)'
tables = query_api.query(query, org="IHPC")
for table in tables:
  for record in table.records:
    print (record.values) """

for value in range(5):
  point = (
    Point("home3")
    .tag("room", "kitchen")
    .field("msg", "message${value}")
  )
  write_api.write(bucket=bucket, org="IHPC", record=point)
  time.sleep(3) # separate points by 1 second 