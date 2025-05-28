lint:
	uv run -m ruff check .

test:
	uv run -m pytest

format:
	uv run -m ruff check --fix .

all: lint test format
