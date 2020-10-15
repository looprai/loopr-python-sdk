lint:
	set -e
	set -x
	flake8 loopr
	black --check loopr --diff
	isort --check-only loopr

format:
	set -e
	isort --force-single-line-imports loopr tests
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place loopr tests
	black loopr tests
	isort loopr tests

test:
	pytest --cov=loopr tests/