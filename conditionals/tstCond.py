def tstIf(num1,num2):
    if (num1 < num2):
      retVal="{0} is less than {1}".format(num1, num2)
    elif (num1 > num2):
      retVal="{0} is less than {1}".format(num2,num1)
    else:
        retVal="{0} and {1} are equal".format(num1,num2)
      
    return retVal


if __name__ == '__main__':
    num1=input("Enter Number 1 : ")
    num2=input("Enter Number 2 : ")
    
    print(tstIf(num1,num2))
    
    exit(1)