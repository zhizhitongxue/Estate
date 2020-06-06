include .env
export $(shell sed 's/=.*//' .env)

all:
	docker-compose up --force-recreate -d --build
