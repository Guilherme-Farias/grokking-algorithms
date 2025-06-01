lint:
	uv run -m ruff check .

test:
	uv run -m pytest

test_coverage:
	uv run -m pytest --cov=src --cov-config=.coveragerc --cov-report=html tests/

format:
	uv run -m ruff check --fix .

all: lint test_coverage format
