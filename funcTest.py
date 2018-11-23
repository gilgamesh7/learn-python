'''
Created on 23/11/2018

@author: Maya
'''
def myFunc():
   print("SimpleFunc, no args, no returns")

def myFunc2(arg1,arg2):
    mulVar=arg1*arg2
    print("In the function : " + str(mulVar))
    return(str(mulVar)+ " " + str(arg1) + " " + str(arg2))

def funcCatStr(*args):
    resultStr =""
    for myStr in args:
        resultStr = resultStr + myStr
        
    return(resultStr)

if __name__ == '__main__':
    myFunc()
    print("In Main : " + myFunc2(5,6))
    print("Result of cat strings 1 : " + funcCatStr("A ", "B ", "C"))
    print("Result of cat strings 1 : " + funcCatStr("A ", "B ", "C","D"))
    