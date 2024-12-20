.PHONY: dev prod shell-dev check test

dev:
	docker compose up backend

prod:
	docker compose -f docker-compose.yml up backend

shell-dev:
	docker compose run --rm backend /bin/bash

check:
	uv run -- ruff format src/ && \
	uv run -- ruff check src/ --fix && \
	bash run_mypy

test:
	uv run -- coverage run --source=src -m pytest \
	uv run -- coverage report --show-missing \
	uv run -- coverage html --title "${@-coverage}"
