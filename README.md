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

## Run in docker-compose
```
docker-compose up -d
```
