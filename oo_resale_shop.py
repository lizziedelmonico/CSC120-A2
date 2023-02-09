from computer import * 

class ResaleShop:

    # What attributes will it need?
    # empty inventory
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, computer):
        self.inventory.append(computer)

    def sell(self, computer):
        self.inventory.remove(computer)

    def inventory(self, ):
        print(self.inventory)