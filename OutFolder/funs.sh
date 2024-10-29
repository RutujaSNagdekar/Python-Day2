#! /bin/bash
 a=$1
 function check(){
	 res=`expr $i % 2`
	 if [[ $res -eq 0 ]] then
		 echo "even"
         else
		 echo "odd"
	fi
}
check
