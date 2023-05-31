install:
	poetry install

publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


lint-test:
	poetry run flake8 tests

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check:
	selfcheck test lint

build:
	check
	poetry build
