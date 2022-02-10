"""
Give an OOP feel of a fleet of cars: truck, van, sedan
must honk
must report size
"""

class Car:
    def __init__(self):
        self = self

    def honk(self):
        print('Awooga')

    def size(self):
        print('mid-size')
    
    def drive(self):
        print('Let\'s go places')



class Sedan(Car):
    def __init__(self):
        self = self


class Truck(Car):
    def __init__(self):
        self = self

    def honk(self):
        print('Born in Texas')

    def size(self):
        print('Honky Tonk')


class Van(Car):
    def __init__(self, type = None):
        self.type = type

    def honk(self):
        if self.type and self.type == 'vw':
            print('I am Zac Long, hear me roar')
        else:
            print('beep')


    def size(self):
        print('chungus')

zacsChoice = Van('vw')
zacsChoice.honk()
zacsChoice.size()
a = Car()
a.honk()
a.size()
b = Sedan()
b.honk()
b.size()