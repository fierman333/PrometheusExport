default: docker_build

DOCKER_IMAGE ?= 287970063728.dkr.ecr.us-east-1.amazonaws.com/demoproject/prometheus-export
GIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)
GIT_VERSION ?= $(shell git rev-parse --short HEAD)

# If git branch is master set docker image tag to 'latest'
ifeq ($(GIT_BRANCH), master)
	DOCKER_TAG = latest
else
	DOCKER_TAG = $(GIT_BRANCH)
endif

docker_build:
	@docker build \
	  --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
	  --build-arg VERSION=${GIT_VERSION} \
	  -t $(DOCKER_IMAGE):$(DOCKER_TAG) \
	  -t $(DOCKER_IMAGE):$(GIT_VERSION) \
	  -f ./Dockerfile \
	  .

docker_push:
	# Push to AWS ECR repository
	docker push $(DOCKER_IMAGE):$(DOCKER_TAG)
	docker push $(DOCKER_IMAGE):$(GIT_VERSION)

test:
	docker run --rm $(DOCKER_IMAGE):$(DOCKER_TAG) --version
