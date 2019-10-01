#!/usr/bin/env bash

docker run -it --volume="`pwd`:/app" --workdir '/app' daskdev/dask:2.3.0 python -ic 'from transform import *'
