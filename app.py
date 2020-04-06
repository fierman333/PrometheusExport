import time
import requests
import logging
from os import environ
from prometheus_client.core import GaugeMetricFamily, HistogramMetricFamily, REGISTRY
from prometheus_client import make_wsgi_app
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

sum_response_time={}
count_requests={}
count_bucket={}
buckets=['1', '10', '100', '+Inf']
response_statuses=[0,1]
req_type="GET"
req_timeout=5

if "HTTP_URIS" in environ:
  urls = environ.get("HTTP_URIS").split()
else:
  urls=["https://httpstat.us/200", "https://httpstat.us/503"]

FORMAT = "%(asctime)s %(levelname)-8s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

def initalize():
  for url in urls:
    sum_response_time[url]={}
    count_requests[url]={}
    count_bucket[url]={}
    for res_status in response_statuses:
      sum_response_time[url][res_status]=0
      count_requests[url][res_status]=0
      count_bucket[url][res_status]={}
      for key in range(len(buckets)):
        count_bucket[url][res_status][key]=0

class CustomCollector(object):
    def collect(self):
      for url in urls:
          response = requests.request(req_type, url, timeout=req_timeout)
          status_code = response.status_code
          response_time = response.elapsed.total_seconds()
          if status_code == 200:
            success_status = 1
          else:
            success_status = 0
          status_code_str = str(status_code)

          sum_response_time[url][success_status] += response_time
          sum_response_time_ms = sum_response_time[url][success_status]
          
          count_requests[url][success_status] += 1
          total_count = count_requests[url][success_status]

          for key in range(len(buckets)-1):
            if response_time <= int(buckets[key]):
              count_bucket[url][success_status][key] += 1
 
          g = GaugeMetricFamily("sample_external_url_up", 'Sample external URL up status', labels=['url','code','method'])
          g.add_metric([url, status_code_str, req_type], success_status)
          yield g

          c = GaugeMetricFamily("sample_external_url_response_ms", 'Sample external URL response in ms', labels=['url','code','method'])
          c.add_metric([url, status_code_str, req_type], response_time)
          yield c

          d = HistogramMetricFamily("sample_external_url_response_ms", 'Sample external URL response bucket in ms', labels=['url','code','method'])
          d.add_metric(
            [url, status_code_str, req_type],
            buckets=[
              (buckets[0], count_bucket[url][success_status][0]),
              (buckets[1], count_bucket[url][success_status][1]),
              (buckets[2], count_bucket[url][success_status][2]),
              (buckets[3], total_count)
            ],
            sum_value=sum_response_time_ms
          )
          yield d

          logging.info("GET: %s", url)

# initialize user arrays
initalize()

# register custom collectors
REGISTRY.register(CustomCollector())

# initalize flask app
app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

# Default path should return '200' http status
@app.route('/')
def main():
    return "OK"
