'''
Created on 11/12/2018

@author: T810235
'''
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def tstFileOS():
    print("Current OS : {0}".format(os.name))
    
    print("Oracle directory exists ? : {0}".format(path.exists("C:\oracle")))
    
    print("Oracle is a file ? : {0}".format(path.isfile("c:\oracle")))
    
    print("Oracle is a directory ? : {0}".format(path.isdir("c:\oracle")))
    
    print("Current Directory : {0}".format(os.getcwd()))
    print("Files in {0} : {1}".format(os.getcwd(),os.listdir(os.getcwd())))
    
    for fileName in os.listdir(os.getcwd()) :
        timeMod=time.ctime(path.getmtime(fileName))
        print("File {0} modified on : {1}".format(fileName,timeMod))
        timeDiff=datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(fileName))
        print("It was modified {0}  ago".format(timeDiff))
    
    return(1)
    
if __name__ == '__main__':
    tstFileOS()

exit(1)