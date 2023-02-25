### Bafen
```
git clone https://github.com/xg590/bafen.git
```
1. Build or load dockerized [mitmproxy](https://github.com/xg590/tutorials/blob/master/Docker/mitmproxy.md) 
```
cd bafen/proxy
docker run --name bafen_proxy --interactive --tty --publish 8080:8080      \
           --mount type=bind,src=${PWD}/addons.py,target=${HOME}/addons.py \
           mitmproxy mitmproxy --listen-host 0.0.0.0  -s ${HOME}/addons.py
```
2. Build or load dockerized [jupyter](https://github.com/xg590/tutorials/blob/master/Docker/jupyter.md)
```
cd ../flask
docker run -it --name cool123 jupyter bash &
sleep 10; docker cp cool123:/home/$NEWUSER/dev/cfg dev
cat << EOF > dev/cfg/jupyter_notebook_config.py
c.NotebookApp.ip = '*'
c.NotebookApp.password = 'sha1:ffed18eb1683:ee67a85ceb6baa34b3283f8f8735af6e2e2f9b55'
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '/home/$NEWUSER/dev'
EOF
docker run --name bafen_flask -itp 8888:8888 -p 5000:5000            \
           -v $PWD/dev:/home/newuser/dev                             \
           -v $PWD/new_site_packages:/home/newuser/new_site_packages \
           jupyter bash
```
* Daily Op
```
docker rm $(docker container ls -f 'status=exited' --quiet) # remove exited containers
docker start --attach bafen_proxy
docker start --attach bafen_flask
```