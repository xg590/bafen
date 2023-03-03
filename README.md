* First Run
```
git clone https://github.com/xg590/bafen.git
cd bafen
docker build -t bafen .
docker run  --name bafen --interactive --tty --publish 8080:8080                              \
            --mount type=bind,src=${PWD}/addons.py,target=/home/username123/addons.py         \
            --mount type=bind,src=${PWD}/downloader.py,target=/home/username123/downloader.py \
			-v ${PWD}/audio:/home/username123/audio bafen bash

python downloader.py &
mitmproxy --set console_eventlog_verbosity=error --listen-host 0.0.0.0 -s addons.py
```
* Daily Op
```
docker start --attach bafen
docker rm $(docker container ls -f 'status=exited' --quiet) # remove exited containers
```
* Note 
  1. Each time a new container is created, mitmproxy will generate a new certificate
