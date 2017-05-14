FROM andrewosh/binder-base

MAINTAINER Matthew Feickert <matthew.feickert@cern.ch>

USER root

# Use Python3
RUN conda env list
RUN source activate python3
RUN conda env list
RUN conda list
RUN python --version
