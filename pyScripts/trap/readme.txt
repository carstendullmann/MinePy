# See https://store.docker.com/images/1ae86987-df14-4741-9433-d9602a4da995?tab=description
# See https://pip.readthedocs.io/en/1.1/requirements.html
# the trap can be run by building the dockerfile in this directory with these two docker commands:

docker build -t trap .
docker run --it --rm --name trap trap

OR (non blocking):

docker build -t trap .
docker run -d --restart=unless-stopped --name trap trap

OR (to avoid logs filling the disk):

docker build -t trap .
docker run -d --restart=unless-stopped --log-opt max-size=10m --name trap trap

