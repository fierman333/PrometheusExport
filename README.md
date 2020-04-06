# PrometheusExport
Prometheus Export HTTPS status

> Export HTTP(S) endpoints status and response time metrics to prometheus

## Local development
### Prerequisites
- python3
- pip3

### Install app dependencies
```
pip3 install --user -r requirements.txt
```

### Run unit tests
```
python3 tests/test.py
```

### Run app service
```
uwsgi --http 127.0.0.1:8000 --wsgi-file app.py --callable app_dispatch
```

## Build docker image
```
make docker_build
```

## Push docker image (only as developer of this service)
### Login to docker repository
```
docker login -u $user
```

### Push docker image to logged docker repository
```
make docker_push
```

## Run all services in minikube
### Install 'prometheus-export' app service
https://github.com/fierman333/PrometheusExport/blob/master/charts/prometheus-export/README.md

### Install 'prometheus' metrics server
https://github.com/fierman333/PrometheusExport/blob/master/charts/prometheus/README.md

### Install 'grafana' monitoring server
https://github.com/fierman333/PrometheusExport/blob/master/charts/grafana/README.md

## Screenshots
### Prometheus server

![prometheus all metrics](/screenshots/prometheus/prometheus_all_metrics.png?raw=true "Prometheus all metrics")
![prometheus url up](/screenshots/prometheus/prometheus_url_up.png?raw=true "Prometheus url up")
![prometheus response ms](/screenshots/prometheus/prometheus_response_ms.png?raw=true "Prometheus response ms")
![prometheus response ms sum](/screenshots/prometheus/prometheus_response_ms_sum.png?raw=true "Prometheus response ms sum")
![prometheus response count](/screenshots/prometheus/prometheus_response_ms_count.png?raw=true "Prometheus response count")
![prometheus response bucket](/screenshots/prometheus/prometheus_response_ms_bucket.png?raw=true "Prometheus response bucket")

### Grafana server
![grafana all](/screenshots/grafana/grafana_all.png?raw=true "Grafana all")
![grafana url up](/screenshots/grafana/grafana_url_up.png?raw=true "Grafana url up")
![grafana response ms](/screenshots/grafana/grafana_response_ms.png?raw=true "Grafana response ms")
![grafana response ms bucket](/screenshots/grafana/grafana_response_ms_bucket.png?raw=true "Grafana response ms bucket")
