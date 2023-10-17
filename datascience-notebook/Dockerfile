FROM jupyter/datascience-notebook

RUN conda update -n base conda && conda install jupyter

RUN conda install nb_conda_kernels nb_conda

# install jupyterlab git extension
RUN pip install --upgrade jupyterlab-git

# instal poetry

ENV POETRY_HOME=/etc/poetry

# echo current user

USER root

RUN curl -sSL https://install.python-poetry.org | python3 -
# add poetry to path
ENV PATH="${POETRY_HOME}/bin:${PATH}"

USER jovyan