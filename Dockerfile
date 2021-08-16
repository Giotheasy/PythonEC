FROM continuumio/miniconda3:latest
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN conda install --file requirements.txt

