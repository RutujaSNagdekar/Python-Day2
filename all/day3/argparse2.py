
#!/usr/bin/python3
import subprocess as ss
import sys
import argparse


def fun1 (*args):
    parser = argparse.ArgumentParser(description= "This is tool to dash")
    #parser.add_argument("-d", type=str, help="Proovide Target", required=False)
    parser.add_argument("-c",type=str,nargs = '+', help="Please enter command", required = True)
    a=parser.parse_args()
    return a.c



def fun2():
    aa = fun1()
    process = ss.Popen(aa, stdout = ss.PIPE, stderr = ss.PIPE, text =  True)
    a,b = process.communicate();
    print("Process a", a)
    print("Process b",b)
    print("Process Object", process)

fun1(sys.argv[2:])
fun2()

                       
