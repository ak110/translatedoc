
help:
	@cat Makefile

update:
	poetry update
	$(MAKE) test

format:
	poetry run pyfltr --exit-zero-even-if-formatted --commands=pyupgrade,autoflake,isort,black,pflake8

test:
	poetry install --no-interaction
	poetry run pyfltr --exit-zero-even-if-formatted
