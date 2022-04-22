
if [[ $1 == "" ]];then
    echo "Usage: ./isleap.sh year"
elif [[ `expr $1 % 400` == '0'  ]];then
    echo "$1 is a leap year"
elif [[ `expr $1 %  4` == '0' && `expr $1 % 100` != '0' ]];then
    echo "$1 is a leap year"

else
    echo "$1 is not a leap year"
fi

