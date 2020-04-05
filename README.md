# PrometheusExport
Prometheus Export HTTPS status

## Run app service locally
```
uwsgi --http 127.0.0.1:8000 --wsgi-file app.py --callable app_dispatch
```

## Build docker image
```
make docker_build
```

## Push docker image (only as developer of this service)
### Login to docker repository
docker login -u $user

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
