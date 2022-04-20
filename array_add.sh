#!/bin/bash

linux_distros=("Ubuntu" "Fedora" "Red-Hat")
echo ${linux_distros[*]}

printf "\n"

linux_distros+=("OpenBSD") # adding element in array
echo ${linux_distros[*]}

unset linux_distros[2] # deleting an element
echo ${linux_distros[*]}
