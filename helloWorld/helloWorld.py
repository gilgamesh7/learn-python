def myMain():
   print ("In God We Trust")
   print ("Gorgonzola")
   print (__name__)

   global myVar
   myVar="assigned globally"
   print("In main : " + str(myVar))

def myFunc():
    myVar=0
    print("In myFunc : " + str(myVar))


if __name__=="helloWorld.helloWorld":
   myMain()
   myFunc()

exit(1)