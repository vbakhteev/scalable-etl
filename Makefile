WORKERS = 2

deploy:
	    docker-compose up -d --scale cleaner=$(WORKERS)

downup:
	    docker-compose down && docker-compose up -d --build