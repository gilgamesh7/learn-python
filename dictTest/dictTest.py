'''
Created on 5/12/2018

@author: T810235
'''

def dictTest(dictIndex):
    myDict={}
    myDict['i']="In"
    myDict['g']="God"
    myDict['w']="We"
    myDict['t']="Trust"
    
    retVal = myDict.get(dictIndex,"All Others Must Pay In Cash!")
    
    return(retVal)

if __name__ == '__main__':
    print("Test 1 : {0}".format(dictTest('i')))
    print("Test 2 : {0}".format(dictTest('g')))
    print("Test 3 : {0}".format(dictTest('w')))
    print("Test 4 : {0}".format(dictTest('t')))
    print("Test 4 : {0}".format(dictTest('x')))
           
exit(1)