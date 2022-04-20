#!/bin/bash

if [[ $1 == "" ]];then
    echo "Usage: ./sorted_num.sh num.txt"
else
    sort -h $1 # human numeric sorted
fi
