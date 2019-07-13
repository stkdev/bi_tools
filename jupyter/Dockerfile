ARG BASE_CONTAINER=jupyter/datascience-notebook:abdb27a6dfbb
FROM $BASE_CONTAINER

# LABEL maintainer="stkdev <stkdev@dammy.com>"

USER $NB_UID

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install --quiet --yes \
    'qt' \
    'pyqt' \
    'pymysql=0.9.3' && \
    conda remove --quiet --yes --force qt pyqt && \
    conda clean --all -f -y && \
    jupyter labextension install @lckr/jupyterlab_variableinspector@0.2.1 && \
    jupyter labextension install @jupyterlab/toc@0.6.0 && \
    jupyter labextension install @jupyterlab/git@0.6.0 && \
    pip install --upgrade jupyterlab-git && \
    jupyter serverextension enable --py jupyterlab_git && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

USER $NB_UID
