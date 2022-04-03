

deploy: check-env
	    docker-compose up -d --scale cleaner=$(WORKERS)

down:
	    docker-compose down

downup:
	    docker-compose down && docker-compose up -d --build

check-env:
ifndef WORKERS
    $(error WORKERS is undefined)
endif