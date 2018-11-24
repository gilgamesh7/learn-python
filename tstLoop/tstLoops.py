def tstWhileLoop():
    i=0
    while(i<=10):
        print("{0}".format(i))
        i=i+1
        
    return(1)

def tstForLoops():
    for i in range (1,11,2):
        print("{0}".format(i))
    
    for i in range(1,31):
        if (i%2 == 0):
            continue
        print("{0}".format(i))
        
    myList=["Luxuria","Gula","Avaritia","Acedia","Ira","Invidia","Superbia"]
    for i,s in enumerate(myList):
        print("{0}{1}{2}".format(i,"--",s))
       
    return(1)

if __name__ == '__main__':
    tstWhileLoop()
    tstForLoops()
    
exit(1)