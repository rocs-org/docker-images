FROM python:3.11-slim

# install make
RUN apt update && apt install -y make curl unixodbc-dev

# install poetry
ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# add poetry to path and configure poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"
RUN poetry config virtualenvs.create false

# create user testuser
RUN adduser testuser

# set workdir
WORKDIR /home/testuser

USER testuser

