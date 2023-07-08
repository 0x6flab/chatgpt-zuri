DOCKER_IMAGE_NAME_PREFIX ?= ghcr.io/0x6flab/chatgpt-zuri
SERVICE = telegram-bot
VERSION ?= $(shell git describe --abbrev=0 --tags)

define make_docker
	docker build --no-cache --tag=$(DOCKER_IMAGE_NAME_PREFIX)/$(SERVICE):$(1) -f telegram/Dockerfile telegram
endef

define docker_push
	docker push $(DOCKER_IMAGE_NAME_PREFIX)/$(SERVICE):$(1)
endef

.PHONY: build

build:
	$(call make_docker,latest)

cleandocker:
	docker-compose -f docker-compose.yaml down -v --remove-orphans

docker_push:
	$(call make_docker,$(VERSION))
	$(call docker_push,$(VERSION))
	$(call make_docker,latest)
	$(call docker_push,latest)

rundev:
	cd telegram && python3 app.py

run:
	docker-compose -f docker-compose.yaml up --env-file telegram/.env -d
