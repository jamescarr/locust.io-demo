import os
from influxdb import InfluxDBClient
from datetime import datetime

class Reporter(object):

    def __init__(self):
        self._client = InfluxDBClient('influxdb', 8086, 'root', 'root', 'example')
        self._client.create_database('example')
        self._user_count = 0


    def hatch_complete(self, user_count):
        self._user_count = user_count


    def request_success(self, request_type, name,
                        response_time, response_length):
        points = [{
            "measurement": "request_success_duration",
            "tags": {
                "request_type": request_type,
                "name": name
            },
            "time": datetime.now().isoformat(),
            "fields": {
                "value": response_time
            }
        },
        {
            "measurement": "user_count",
            "time": datetime.now().isoformat(),
            "fields": {
                "value": self._user_count
            }
        }]
        self._client.write_points(points)
