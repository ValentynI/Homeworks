class Ship:
    def __init__(self, fuel, swim_range):
        self.fuel = fuel
        self.swim_range = swim_range

    def swim(self):
        if self.fuel > 0:
            print('Wvsssss')
            self.fuel -= 1
        else:
            print('No fuel!')


class WarShip(Ship):
    def __init__(self, gun, fuel, swim_range):
        super(WarShip, self).__init__(fuel, swim_range)
        self.gun = gun

    def gun(self):
        if self.gun > 0:
            print('Boom')
            self.gun -=1
        else:
            print('No Boom!')

Wakeful = WarShip(10, 400, 10000)
Wakeful.swim()
