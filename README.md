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
```
aws configure --profile demoproject-developer
AWS Access Key ID [None]: xxx
AWS Secret Access Key [None]: xxx
Default region name [None]: us-east-1
Default output format [None]:
```

## Login to docker AWS ECR repository
```
$(aws ecr get-login --no-include-email --profile demoproject-developer)
```

## Build docker image
```
make docker_build
```

## Push docker image
```
make docker_push
```
