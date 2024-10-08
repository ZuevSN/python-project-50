install:
	poetry install

gendiff:
	poetry run python -m gendiff.scripts.gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml