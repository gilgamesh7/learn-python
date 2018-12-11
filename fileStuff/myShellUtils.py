'''
Created on 11/12/2018

@author: T810235
'''
import os
from os import path
import shutil

def myShellUtils(myFileName):
    if path.exists(myFileName):
        retVal=myFileName+" Exists"
    else :
        retVal=myFileName+" does not exist"
        
    if path.exists(myFileName):
        src=myFileName
        dst=myFileName+".bak"
        retVal=os.listdir()
            
    return(retVal)

if __name__ == '__main__':
    print(myShellUtils("C:\doesnotexist.txt"))
    myPath=os.getcwd()
    myFile=myPath+"fileOS.py"
    myShellUtils(myFile)

exit(1)