# [AnimeGANv2-pytorch](https://github.com/bryandlee/animegan2-pytorch) in docker

This repository wraps up **AnimeGANv2-pytorch** inside a docker image so that it can be run as a server or a lambda function.

## Lambda usage -

To build it as a lambda function, run -
```
./build_and_run.sh lambda
```
this will build the docker image and run the lambda function (locally) reachable at port 9000.

test it -
```
python test.py lambda
```
and we should get an `output.jpeg` file in the project root folder.

## Server usage -

To build it as a server api, run -
```
./build_and_run.sh server
```
this will build the docker image and run a python server reachable at port 9000.

test it -
```
python test.py server
```
and we should get `output.jpeg` file in the project root folder.