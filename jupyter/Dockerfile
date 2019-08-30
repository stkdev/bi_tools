ARG BASE_CONTAINER=jupyter/datascience-notebook:abdb27a6dfbb
FROM $BASE_CONTAINER

# LABEL maintainer="stkdev <stkdev@dammy.com>"

USER root

RUN apt update \
    && apt install -yq graphviz \
    && rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN jupyter labextension install @lckr/jupyterlab_variableinspector@0.2.1 && \
    jupyter labextension install @jupyterlab/toc@0.6.0 && \
    jupyter labextension install @jupyterlab/git@0.6.0 && \
    pip install --upgrade jupyterlab-git && \
    jupyter serverextension enable --py jupyterlab_git && \
    npm cache clean --force

RUN python3 -m pip install \
    PyMySQL==0.9.3 \
    dtreeviz==0.6 \
    folium==0.10.0 \
    japanize-matplotlib \
    jismesh==2.0.0

USER $NB_UID

