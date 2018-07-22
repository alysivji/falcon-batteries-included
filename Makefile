help:
	@echo 'Makefile for managing web application                        '
	@echo '                                                             '
	@echo 'Usage:                                                       '
	@echo ' make build      build images                                '
	@echo ' make up         creates containers and starts service       '
	@echo ' make start      starts service containers                   '
	@echo ' make stop       stops service containers                    '
	@echo ' make down       stops service and removes containers        '
	@echo '                                                             '
	@echo ' make migrate    run migrations                              '
	@echo ' make test       run tests                                   '
	@echo ' make test_cov   run tests with coverage.py                  '
	@echo ' make test_fast  run tests without migrations                '
	@echo ' make lint       run flake8 linter                           '
	@echo '                                                             '
	@echo ' make attach     attach to process inside service            '
	@echo ' make logs       see container logs                          '
	@echo ' make shell      connect to api container in new bash shell  '
	@echo ' make dbshell    connect to postgres inside db container     '
	@echo '                                                             '

build:
	docker-compose build

up:
	docker-compose up -d api db

start:
	docker-compose start api db

stop:
	docker-compose stop

down:
	docker-compose down

attach: ## Attach to web container
	docker attach `docker-compose ps -q api`

logs:
	docker logs `docker-compose ps -q api`

shell: ## Shell into web container
	docker-compose exec api bash

shell-ipython: ## Shell into ipython with falcon context
	docker-compose exec api python shell.py

shell-db: ## Shell into postgres process inside db container
	docker-compose exec db psql -w --username "sivdev_user" --dbname "sivdev"

migration: up ## Create migrations using alembic
	docker-compose exec api alembic revision --autogenerate -m "$(m)"

migrate-up: up ## Run migrations using alembic
	docker-compose exec api alembic upgrade head

migrate-down: up ## Rollback migrations using alembic
	docker-compose exec api alembic downgrade -1

test: migrate
	docker-compose exec api pytest

test_cov: migrate
	docker-compose exec api pytest --verbose --cov

test_cov_view: migrate
	docker-compose exec api pytest --cov --cov-report html && open ./htmlcov/index.html

test_fast: ## Can pass in parameters using p=''
	docker-compose exec api pytest $(p)

# Flake 8
# options: http://flake8.pycqa.org/en/latest/user/options.html
# codes: http://flake8.pycqa.org/en/latest/user/error-codes.html
max_line_length = 99
lint: up
	docker-compose exec api flake8 \
		--max-line-length $(max_line_length)
