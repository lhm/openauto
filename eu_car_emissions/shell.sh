#!/usr/bin/env bash

docker run -it --volume="`pwd`:/app" --workdir '/app' amancevice/pandas python -i -c 'import numpy as np; import pandas as pd'
