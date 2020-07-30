ARG BASE_CONTAINER=jupyter/datascience-notebook:3b1f4f5e6cc1
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

RUN git clone --recursive https://github.com/ibayer/fastFM.git \
    && cd fastFM \
    && pip install -r ./requirements.txt \
    && make \
    && PYTHON=python3 make \
    && pip install . \
    && cd .. \
    && rm -rf /tmp/fastFM

WORKDIR /home/jovyan

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN jupyter labextension install @lckr/jupyterlab_variableinspector && \
    jupyter labextension install @jupyterlab/toc@4.0.0 && \
    jupyter labextension install ipyvolume && \
    jupyter labextension install @jupyterlab/git@0.20.0 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@2.0.0 jupyter-leaflet@0.12.6 && \
    pip install --upgrade jupyterlab-git==0.20.0 && \
    jupyter serverextension enable --py jupyterlab_git && \
    jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    npm cache clean --force

RUN python3 -m pip install \
    PyMySQL==0.9.3 \
    dtreeviz==0.8.2 \
    ipyleaflet==0.12.6 \
    folium==0.11.0 \
    japanize-matplotlib==1.1.2 \
    jismesh==2.1.0 \
    mecab-python3==0.996.5 \
    gensim==3.8.3 \
    redash_dynamic_query==1.0.4 \
    wordcloud==1.7.0 \
    tqdm==4.45.0 \
    geopandas==0.7.0 \
    plotly==4.7.1 \
    python-Levenshtein==0.12.0 \
    ngt==1.11.5 \
    openpyxl==3.0.4 \
    ginza==3.1.1

USER $NB_UID

