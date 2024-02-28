
help:
	@cat Makefile

update:
	poetry update
	$(MAKE) test

format:
	poetry run pyfltr --exit-zero-even-if-formatted --commands=fast

test:
	poetry install --no-interaction
	poetry run pyfltr --exit-zero-even-if-formatted
