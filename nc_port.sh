#!/bin/bash

hit_C () {

printf "\rYikes! Aborting!!" | lolcat
exit
}

trap "hit_C" 2


# if [[ $1 == "" ]];then
#
#         echo "Usage: ./nc_port.sh ip "
#         echo "Usage: ./nc_port ip portnumber"
#
# elif [[ $1 != "" && $2 != "" ]];then
#         nc -zv $1 $2 &>/dev/null
#
#
#         if [[ $? == 0 ]];then
#             echo "Port $2 is open"
#         else
#             echo "Port $2 is closed"
#         fi
# else
#         echo "Hit Control-C to stop scanning!" | lolcat
#         for i in {1..65535};do
#         nc -zv $1 $i &>/dev/null
#         if [[ $? == 0 ]];then
#             echo "Port $i is open"
#         fi
#     done
# fi


if [[ $1 == "" ]];then

        echo "Usage: ./nc_port.sh ip "
        echo "Usage: ./nc_port ip portnumber"

elif [[ $1 != "" && $2 != "" ]];then
        nc -zv $1 $2 &>/dev/null && echo "[+] Port $2 is open"||  echo "[-] Port $2 is closed"


else
        echo "Hit Control-C to stop scanning!" | lolcat
        for i in {1..65535};do
        nc -zv $1 $i &>/dev/null && echo "[+] Port $i is open"
    done
fi
