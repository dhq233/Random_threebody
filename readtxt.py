# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 00:01:40 2024

@author: lenovo
"""





f = open('./三体.txt', 'r',encoding='utf-8')
lineList = f.readlines()
f.close()


lines=[]
for line in lineList:
    
    if  line[0] == "-" or line[0] == "第" or line == "\n":
        continue
    else:
        lines.append("'"+line.replace("\n"," ")+"',\n")
    
f2=open('./三体1.txt','w',encoding='utf-8')
for line in lines:
   if  line[0] == "-" or line[0] == "第" or line == "\n":
       continue
   else: 
       f2.write(line)
f2.close()