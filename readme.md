# Web Interface for Pacparser 
Have you ever wondered "When I access to this URL, Which proxy will I use? Or direct?"
Me helps you.

![](https://raw.githubusercontent.com/kujiy/pacparser-web/master/screenshot.jpg)

## Demo(Currently not working)
https://pacparser-web.herokuapp.com/

This demo answers `Direct` for `http://localhost/`, `PROXY your-company-proxy:8080` for `http://example.com/` and `PROXY your-sub-proxy:3128` for other URL.


## Getting started
1. Clone this repository

    ```sh
    $ git clone https://github.com/kujiy/pacparser-web.git
    ```
1. Update `app/yourpacs.py` with your .pac file URL.

    ```sh
    $ cd pacparser-web
    $ vi app/yourpacs.py
    ```
1. Launch your container

    ```sh
    $ cd pacparser-web
    $ docker-compose up
    ```
1. Access to [http://localhost/](http://localhost/) or  [http://your-docker-host:5000/](http://your-docker-host:5000/) with your browser
 - You can change the port in `docker-compose.yml` .

## How to Use
1. Access your container with browsers
    - [http://localhost/](http://localhost/) or  [http://your-docker-host:5000/](http://your-docker-host:5000/)
1. Select pac file(those are defined in `app/yourpacs.py`) and input target URL then submit
1. You'll get pacparser answer.

## Related projects
- PAC parse engine
 - https://github.com/pacparser/pacparser
- Web server with python
 - https://github.com/tiangolo/uwsgi-nginx-flask-docker
- CSS Framework
 - https://github.com/Dogfalo/materialize

## File architect
- main.py is the main file
- index.html is a template file of the form

### Build procedure
1. `Dockerfile`
 - [The Original image](https://github.com/tiangolo/uwsgi-nginx-flask-docker) has python, flask and ngx. It works with `/app/main.py`.
1. `docker-compose.yml`
 - Replace main.py to mine(works with pacparser).
 - Set proxy to connect internet.
1. `entrypoint.sh`
 -  Download [pacparser](https://github.com/pacparser/pacparser) from github and install(make).


#### Access and what's happen
1. Access to pacparser-web with your browser
1. ngx/uwsgi execute /app/main.py
1. main.py gets query strings of pac file and search url from accessed URL 
1. Download latest pac file(To test with latest one)
1. Get its last modified date with `stat` command(This is just for me)
1. Ask pacparser "Which proxy will you use for this URL?" and get an answer
1. Call html template engine(Flask's render_template)
1. /app/templates/index.html called
1. Show html forms

##### How to debug
Login to the container with `docker exec CONT_NAME -it sh` and change `/app`.
If you change `/app/main.py`, need `supervisorctl restart uwsgi`.
Restarting will be unnecesarry for `/app/templates` .

