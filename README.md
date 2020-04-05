# PrometheusExport
Prometheus Export HTTPS status

## Install aws cli
### Debian/Ubuntu
```
sudo apt install python3-pip
pip3 install awscli
echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc && export PATH=~/.local/bin:$PATH
```

### Windows
Download and install msi package: https://s3.amazonaws.com/aws-cli/AWSCLI64PY3.msi

## Configure AWS CLI profile
### As user/consumer of this service
```
aws configure --profile demoproject-user
AWS Access Key ID [None]: AKIAUGDC2OVYGV5A7GLE
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:
```

### As developer of this service
```
aws configure --profile demoproject-developer
AWS Access Key ID [None]: xxxxxx
AWS Secret Access Key [None]: xxxxxx
Default region name [None]: us-east-1
Default output format [None]:
```

## Login to docker AWS ECR repository
### As user/consumer of this service
```
$(aws ecr get-login --no-include-email --profile demoproject-user)
```

### As developer of this service
```
$(aws ecr get-login --no-include-email --profile demoproject-developer)
```

## Build docker image
```
make docker_build
```

## Push docker image (only as developer of this service)
```
export AWS_PROFILE=demoproject-developer
make docker_push
```

## Run app service locally
```
uwsgi --http 127.0.0.1:8000 --wsgi-file app.py --callable app_dispatch
```

## Run all services in minikube
### Install 'registry-creds' service to allow minikube AWS ECR repository login
https://github.com/fierman333/PrometheusExport/blob/master/charts/registry-creds/README.md

### Install 'prometheus-export' app service
https://github.com/fierman333/PrometheusExport/blob/master/charts/prometheus-export/README.md

### Install 'prometheus' metrics server
https://github.com/fierman333/PrometheusExport/blob/master/charts/prometheus/README.md

### Install 'grafana' monitoring server
https://github.com/fierman333/PrometheusExport/blob/master/charts/grafana/README.md
