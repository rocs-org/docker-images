FROM jupyter/datascience-notebook

RUN conda install nb_conda_kernels nb_conda

# install jupyterlab git extension
RUN pip install --upgrade jupyterlab-git

# instal poetry

ENV POETRY_HOME=/etc/poetry

RUN curl -sSL https://install.python-poetry.org | python3 -
# add poetry to path
ENV PATH="${POETRY_HOME}/bin:${PATH}"
