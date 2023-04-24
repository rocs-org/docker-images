FROM ubuntu:22.04

# install python
RUN apt update && apt install -y python3 python3-pip
RUN python3 --version

# install poetry
ENV POETRY_HOME=/etc/poetry
RUN apt update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

# add poetry to path and configure poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# install aws cli
#RUN mkdir -p /root/.aws
#RUN echo 'region = us-west-2' > /root/.aws/credentials
RUN pip3 install awscli

# install mtr
RUN apt install -y mtr