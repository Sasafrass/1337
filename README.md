# 1337
Proud winner of 2k21's ugliest code award TM.

Normal Ranking             |  Cheater Ranking
:-------------------------:|:-------------------------:
![alt text](https://github.com/Sasafrass/1337/blob/master/img/normal.png?raw=true)  |  ![alt text](https://github.com/Sasafrass/1337/blob/master/img/cheat.png?raw=true)

## What
To decide once and for all who's the best 1337'er @ 13:37.

## How
* Docker hub repository
  * https://hub.docker.com/repository/docker/sasafras/1337
* Pull the docker image from the repository
  * docker pull sasafras/1337:latest
* Run the docker image with a volume to your current working directory to persist the image locally
  * docker run -v $(pwd):/usr/app/src/img sasafras/1337:latest
* Enjoy
