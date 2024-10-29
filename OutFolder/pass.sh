#!/bin/bash

pass=$1
if [[  $pass =~ 2.......  ]] && [[ $pass =~ [A-Z] ]] && [[ $pass =~ [a-z] ]] && [[ $pass =~ ([0-9].*){2} ]];then
       echo "Valid Password"
else
 	echo "Invalid Password"
fi

