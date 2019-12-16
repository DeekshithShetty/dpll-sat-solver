#!/bin/sh

#timeout 10s python3 main.py $* ulimit -S -v 4194304

for file in ./benchmarks/*; do
  echo "$(basename "$file")"
  timeout 10s python3 main.py "$file" ulimit -S -v 4194304
  echo "--------------------"
done
