'''
Created on 6/12/2018

@author: T810235
'''
from datetime import datetime

def fileStuff():
    f=open("c:\igwt.txt","a+")
    
    nowTime=datetime.now()
    f.write(str(nowTime)+"\r\n")
    
    for i in range(10):
        f.write("Line" + str(i) + ": In God We Trust" + "\r\n")
    
    f.close()
    
    f=open("c:\igwt.txt","r")
    if f.mode == 'r':
        lineArray=f.readlines()
        for line in lineArray:
            print(line)
    else:
        print("File is not readable")
    
    f.close()
    
    return(1)

if __name__ == '__main__':
    fileStuff()
    
exit(1)