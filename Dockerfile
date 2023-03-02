# syntax=docker/dockerfile:1
FROM python:3
RUN useradd -m username123
USER username123
WORKDIR /home/username123
ENV PATH="/home/username123/.local/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install mitmproxy flask requests pandas 
RUN pip cache purge