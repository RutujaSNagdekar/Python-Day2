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
    return a


def fun2():

    aa = fun1()
    op = ss.getoutput(aa.c)
    print(op)
    if aa.o:
        with open(aa.o, "w") as f1:
            f1.write(op)
        
if __name__ =='__main__':
    #Try and except --- add in this code
    try:
        fun1(sys.argv[1])
    except:
        print("Please Enter Command")
