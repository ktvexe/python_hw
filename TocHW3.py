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
#
#link:
"""
#!/usr/bin/env python

import sys

def MAX_ARG():
        return  3

list_arg=[]
ans =[0,0,0,0,0,0,0,0,0,0]
print ans[0]
for i in range(MAX_ARG()-1):
    tmp =sys.argv[i+1].split('#')
    list_arg.append(tmp)
with open(sys.argv[MAX_ARG()],"r") as fptr:
        for line in fptr:
                for i in range(MAX_ARG()-1):
                        if(line.find(list_arg[i][0])!=-1 and line.find(list_arg[i][1])!=-1):
                                ans[i] +=1

fptr.close()
for i in range(MAX_ARG()-1):
	print sys.argv[i+1],ans[i]

#print list_arg
#print str(list_arg).decode('string_escape')

