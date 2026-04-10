#!/bin/bash
#!usr/bin/python3

# This script is used to get the server stats and print them in a nice format

# Get the server stats
cpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
mem=$(free -m | awk 'NR==2{printf "%.