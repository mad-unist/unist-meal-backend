# Init Project
init:
	/bin/bash scripts/init.sh

# Inside Continaer
migrations:
	python src/manage.py makemigrations $(app)
migrate:
	python src/manage.py migrate $(app)

# Outside Container
dev-up:
	docker-compose -f docker-compose.dev.yml up --build
dev-down:
	docker-compose -f docker-compose.dev.yml down $(args)
dev-shell:
	docker-compose -f docker-compose.dev.yml run --rm app /bin/bash

# test
test:
	docker-compose -f docker-compose.test.yml run --rm app /bin/bash -c "scripts/test.sh $(args)"
	docker-compose -f docker-compose.test.yml down

clean:
	docker container prune -f
	docker rmi $$(docker images -f "dangling=true" -q) -f

# git
commit:
	cz c