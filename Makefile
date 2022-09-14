watch:
	poetry run pytest -v -f -ff -x

test:
	poetry run pytest -v

# lint with black and pylama
lint:
	poetry run black . --check
	poetry run pylama .