import random

## Variables & init
# Dice values
minVal=1
maxVal=6
# Repeated trghrow y/n flag
throw_again=1

while throw_again==1:
    print ("Throwing Dice ...")
    diceOne = random.randint(minVal,maxVal)
    diceTwo = random.randint(minVal,maxVal)
    
    print ("You threw {0} on Dice 1 and {1} on Dice 2".format(diceOne,diceTwo))
    
    checkThrow=input("Do you want to throw again(y/n) ?")
    if checkThrow == 'y':
        throw_again = 1
    else:
        throw_again=0
        