ARG BASE_CONTAINER=jupyter/datascience-notebook:abdb27a6dfbb
FROM $BASE_CONTAINER

# LABEL maintainer="stkdev <stkdev@dammy.com>"

USER root

RUN apt update \
    && apt install -yq graphviz \
    && apt-get install -y swig mecab mecab-ipadic-utf8 libmecab-dev file \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y -a \
    && rm -rf /tmp/mecab-ipadic-neologd

WORKDIR /home/jovyan

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN jupyter labextension install @lckr/jupyterlab_variableinspector@0.2.1 && \
    jupyter labextension install @jupyterlab/toc@0.6.0 && \
    jupyter labextension install @jupyterlab/git@0.6.0 && \
    jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install ipyvolume@0.5.2 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 && \
    pip install --upgrade jupyterlab-git && \
    jupyter serverextension enable --py jupyterlab_git && \
    npm cache clean --force

RUN python3 -m pip install \
    PyMySQL==0.9.3 \
    dtreeviz==0.6 \
    folium==0.10.0 \
    japanize-matplotlib \
    jismesh==2.0.0 \
    mecab-python3==0.996.2 \
    gensim==3.8.0 \
    redash_dynamic_query==1.0.4 \
    wordcloud==1.5.0 \
    tqdm==4.38.0 \
    geopandas==0.6.2 \
    plotly==4.3.0

USER $NB_UID

