# syntax=docker/dockerfile:1
FROM python:3
RUN useradd -m username123
USER username123
WORKDIR /home/username123
ENV PATH="/home/username123/.local/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install jupyter notebook=="6.4.11" jupyter_contrib_nbextensions wheel
RUN pip3 install mitmproxy flask requests pandas matplotlib
RUN pip3 install moviepy pygame
RUN pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
RUN pip3 cache purge
RUN         mkdir -p    /home/username123/script/cfg          
ENV JUPYTER_CONFIG_DIR="/home/username123/script/cfg"
ENV               PATH="/home/username123/script/.new_site_packages/bin:$PATH"
RUN         mkdir       /home/username123/script/.new_site_packages      
ENV         PIP_TARGET="/home/username123/script/.new_site_packages"
ENV         PYTHONPATH="/home/username123/script/.new_site_packages" 
RUN jupyter contrib nbextension install --user