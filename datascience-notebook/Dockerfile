FROM jupyter/datascience-notebook

# change default shell to bash
# RUN chsh -s /bin/bash

# install jupyterlab git extension
RUN pip install --upgrade jupyterlab-git

# instal poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# add poetry to path
ENV PATH="${HOME}/.local/bin:${PATH}"
