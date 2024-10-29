#!/usr/bin/python3

import argparse
import os
import sys
import subprocess as ss

#parser = argparse.ArgumentParser(description= "This is tool to dash")

def fun1 (*args):
    parser = argparse.ArgumentParser(description= "This is tool to dash")
    #parser.add_argument("-d", type=str, help="Proovide Target", required=False)
    parser.add_argument("-c",type=str, help="Please enter command", required = True)
    parser.add_argument("-o", type=str, help="Enter file name", required = False)
    a=parser.parse_args()
    os.system(a.c.lower())
    return a.c


def fun2():
    aa = fun1()
    status = os.system(aa.lower())
    print(status)

    if status==0:
        print("This is a Valid Command")
    
    else:
        print("Not a valid command")





try:
    fun1(sys.argv[2])
except Exception:
    print("Please provide command")








