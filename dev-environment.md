# Dev Environment

This section describes setting up a dev environment.

## Bootstap using Docker

Docker image docker-bpo: <https://github.com/python/docker-bpo>

Docker Hub image: <https://hub.docker.com/r/python/docker-bpo>

Another docker image (not sure its purpose - openshift deploy?) <https://hub.docker.com/r/python/bpo-builder>

### Quickstart

```bash
git clone https://github.com/python/docker-bpo.git
cd docker-bpo
docker pull docker.io/python/docker-bpo
./pull.sh
docker run --rm -it -p 9999:9999 -v `pwd`:/opt/tracker docker.io/python/docker-bpo

# After container mounts the volume
rd-start
```

Three accounts are created: user, developer, coordinator. Login with `pass` as
password.

To view the user interface: <http://localhost:9999>

## From scratch

Python wiki for Tracker - out of date: <https://wiki.python.org/moin/TrackerDevelopment>



### Set Up by Components

Running tests from the repo::

```
python2 run_tests.py
```
