"""
#python homework v1.0
#
#use split method to separate input arguments 10 times, 
#and then use find method to check whether the file has input 
#string or not.
#
#author: Liang-Gu Liu 
#student number:F64011279
#
#link:https://github.com/ktvexe/python_hw
"""
#!/usr/bin/env python

import sys

def MAX_ARG():
        return  11

list_arg=[]
ans =[0,0,0,0,0,0,0,0,0,0]
tmp =sys.argv[1].split(',')
for i in range(MAX_ARG()-1):
        tmp_real =tmp[i].split('#')
        list_arg.append(tmp_real)

with open(sys.argv[2],"r") as fptr:
        for line in fptr:
                for i in range(MAX_ARG()-1):
                        if(line.find(list_arg[i][0])!=-1 and line.find(list_arg[i][1])!=-1):
                                ans[i] +=1
fptr.close()
for i in range(MAX_ARG()-1):
        print list_arg[i][0],"#",list_arg[i][1],",",ans[i]

#print list_arg
#print str(list_arg).decode('string_escape')


