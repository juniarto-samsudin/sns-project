import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

class Writer:
    def __init__(self, url, token, org, bucket):
        self.org = org
        self.write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.write_client.write_api(write_options=SYNCHRONOUS)
        self.bucket = bucket
    def write(self, measurement, tagName,tagValue,  field1, value1, field2, value2):
        point = (
            Point(measurement)
            .tag(tagName, tagValue)
            .field(field1, value1)
            .field(field2, value2)
        )
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)
    def writeWithTime(self, measurement, tagName,tagValue,  field, value, time):
        date_object = datetime.strptime(time, '%Y-%m-%d')
        point = (
            Point(measurement)
            .tag(tagName, tagValue)
            .field(field, value)
            .time(date_object)
        )
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

