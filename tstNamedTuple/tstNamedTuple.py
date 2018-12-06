'''
Created on 6/12/2018

@author: T810235
'''
from collections import namedtuple

def tstNamedTuple():
    Car = namedtuple('Car', 'color mileage')
    my_car = Car('red', 3812.4)
    
    print(my_car.color)
    
    print(my_car.mileage)
    
    print(my_car)
    
    # my_car.color = 'blue'
    
    
    return(0)

if __name__ == '__main__':
    tstNamedTuple()
    
exit(1)