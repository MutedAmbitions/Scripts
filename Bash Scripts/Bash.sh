#!/bin/bash

message="Hello there."
n=0
while [ $n -le 5 ]; do
    # body
    echo "$message"
    sleep 1s
    n=$((n+1))
    echo "$n"
    
done
