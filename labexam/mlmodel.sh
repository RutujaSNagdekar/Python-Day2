#!bin/bash

a=$1

if [[ $a -ge "90" ]];then
        echo "This is highly accurate model"
elif [[ $a -ge "70" && $a -le "90" ]];then
       echo "This model has moderate accuracy"
elif [[ $a -le 70 ]];then
        echo "This model needs improvement"
else
        echo "Invalid input"

fi



