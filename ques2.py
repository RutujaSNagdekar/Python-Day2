#!/usr/bin/python3
import sys
import subprocess as ss
s=sys.argv[1:]


process = ss.Popen(s, stdout = ss.PIPE, stderr = ss.PIPE, text =  True)
a,b = process.communicate();
print("Process a", a)
print("Process b",b)
print("Process Object", process)




                                                                                                                                                                  
                                                                                                                                                                  
                                
