import unittest

from prometheus_client.core import (
    GaugeMetricFamily, HistogramMetricFamily,  CollectorRegistry, UntypedMetricFamily
)

url="https://httpstat.us/200"
status_code="200"
req_type="GET"
success_status=1
response_time=0.829605
sum_response_time_ms=121.326154
buckets={'1': 1, '10':10, '100':100, '+Inf': 110}

class TestEndpointStatus(unittest.TestCase):
  def setUp(self):
    self.registry = CollectorRegistry()

  def custom_collector(self, metric_family):
    class CustomCollector(object):
      def collect(self):
        return [metric_family]
    self.registry.register(CustomCollector())

  def test_endpoint_statuses(self):
    cmf = GaugeMetricFamily("sample_external_url_response_ms", 'Sample external URL up status', labels=['url','code','method'])
    cmf.add_metric([url, status_code, req_type], success_status)
    self.custom_collector(cmf)
    self.assertEqual(1, self.registry.get_sample_value('sample_external_url_response_ms', {'url': url,'code': status_code, 'method': req_type}))

  def test_endpoint_response(self):
    cmf = GaugeMetricFamily("sample_external_url_response_ms", 'Sample external URL up status', labels=['url','code','method'])
    cmf.add_metric([url, status_code, req_type], response_time)
    self.custom_collector(cmf)
    self.assertEqual(0.829605, self.registry.get_sample_value('sample_external_url_response_ms', {'url': url,'code': status_code, 'method': req_type}))

  def test_endpoint_response_bucket(self):
    cmf = HistogramMetricFamily("sample_external_url_response_ms", 'Sample external URL response bucket in ms', labels=['url','code','method'])
    cmf.add_metric(
      [url, status_code, req_type],
      buckets=[
        ('1', buckets['1']),
        ('10', buckets['10']),
        ('100', buckets['100']),
        ('+Inf', buckets['+Inf'])
      ],
      sum_value=sum_response_time_ms
    )

    self.custom_collector(cmf)
    self.assertEqual(1, self.registry.get_sample_value('sample_external_url_response_ms_bucket', {'url': url,'code': status_code, 'method': req_type, 'le': '1'}))
    self.assertEqual(10, self.registry.get_sample_value('sample_external_url_response_ms_bucket', {'url': url,'code': status_code, 'method': req_type, 'le': '10'}))
    self.assertEqual(100, self.registry.get_sample_value('sample_external_url_response_ms_bucket', {'url': url,'code': status_code, 'method': req_type, 'le': '100'}))
    self.assertEqual(110, self.registry.get_sample_value('sample_external_url_response_ms_bucket', {'url': url,'code': status_code, 'method': req_type, 'le': '+Inf'}))
    self.assertEqual(110, self.registry.get_sample_value('sample_external_url_response_ms_count', {'url': url,'code': status_code, 'method': req_type}))
    self.assertEqual(121.326154, self.registry.get_sample_value('sample_external_url_response_ms_sum', {'url': url,'code': status_code, 'method': req_type}))
        
if __name__ == '__main__':
  unittest.main()
