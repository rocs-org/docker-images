watch:
	poetry run pytest -v -f -ff -x

test:
	poetry run pytest '${dir}' -v

# lint with black and pylama
lint:
	poetry run black . --check
	poetry run pylama .

# build the dockerfile from one folder
build:
	docker build ${folder}