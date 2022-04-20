#!/bin/bash

#cat $1 |  tr '[:lower:]' '[:upper:]'
cat $1 | tr a-z A-Z

# awk '{print toupper($0)}' $1
