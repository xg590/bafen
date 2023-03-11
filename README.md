### First Run
```
git clone https://github.com/xg590/bafen.git
cd bafen
docker build -t bafen .
docker run  --name bafen --interactive --tty          \
            --publish 8080:8080 --publish 8888:8888   \
			-v ${PWD}/script:/home/username123/script \
			bafen bash
``` 
### Daily Op
* Start the container
```
docker start bafen && docker attach bafen
```
* Download audio file
```
python script/downloader.py &
mitmproxy --set console_eventlog_verbosity=error --listen-host 0.0.0.0 -s script/addons.py
```
* Edit and upload (oauth2_user_credentials.json and playerlist_id.txt are required for Youtube uploading)
```
kill -15 %1 && sleep 3 && jobs && jupyter-notebook
```
### Note
  1. Each time a new container is created, mitmproxy will generate a new certificate
