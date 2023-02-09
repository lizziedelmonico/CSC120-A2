class Computer:

    # What attributes will it need?
    
  

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    
    def refurbish(self):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 400
        elif self.year_made < 2018:
            self.price = 505
        else:
            self.price = 807

    def update_price(self, new_price):
        self.price = new_price

    def update_os(self, new_os):
        self.operating_system = new_os

    