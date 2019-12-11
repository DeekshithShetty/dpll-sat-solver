#!/bin/sh

##### C++
echo "C++"
./solve-cpp $*

##### Java
echo "Java"
java Solver $*

##### Python
echo "Python"
python3 example.py $*