# Container's default name
NAME=restapi_test

# Docker image default name
IMAGE=test/$(NAME)

# Mount localfile system
LOCAL_OPTS=-v $(shell pwd):/opt/restapi_test -e PYTHONPATH="/opt/restapi_test"

# Build image
.PHONY: build
build:
	@echo "--> Building $(NAME)"
	docker build -t $(IMAGE) .

# Stop container
.PHONY: stop
stop:
	@echo "--> Stopping $(NAME)"
	docker kill $(NAME) || true

# Start container
.PHONY: start
start:
	@echo "--> Starting $(NAME)"
	docker start $(NAME)

# Remove container
.PHONY: rm
rm:
	@echo "--> Removing container $(NAME)"
	docker rm -f $(NAME) || true

# Run container and provide a Shell terminal
.PHONY: local
local:
	@echo "--> Starting $(NAME)"
	docker run $(LOCAL_OPTS) --name $(NAME) --env-file secrets.ini -it $(IMAGE) /bin/bash

# Local development
.PHONY: dev
dev: stop rm build local

# Run container and start the application using uvicorn
.PHONY: server
server:
	@echo "--> Starting $(NAME)"
	docker run $(LOCAL_OPTS) --name $(NAME) -p 8080:8080 --env-file secrets.ini -it $(IMAGE) /bin/bash suites/all_tests.sh

# Run the application
.PHONY: run
run: stop rm build server