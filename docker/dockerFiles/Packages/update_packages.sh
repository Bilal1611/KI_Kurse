#!/bin/bash

for i in $(cat $1); do
    echo "RUN pip install $i"
done
