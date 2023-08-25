FILES := src tests

.PHONY: format
format:
	poetry run black $(FILES)
	poetry run ruff --fix $(FILES)

.PHONY: lint
lint:
	poetry run black --check $(FILES)
	poetry run ruff $(FILES)
	poetry run mypy $(FILES)

.PHONY: test
test:
	poetry run pytest --cov=src --cov-report=term-missing --junitxml=test-results/test-results.xml --cov-branch tests

.PHONY: dev
dev:
	poetry run uvicorn src.handler:app --reload
