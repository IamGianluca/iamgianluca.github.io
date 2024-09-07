install:
	uv pip compile --all-extras pyproject.toml -o requirements.txt && \
	uv pip sync requirements.txt && \
	uv pip install -e . 

check: format lint

format:
	ruff format .

lint:
	ruff check --fix
