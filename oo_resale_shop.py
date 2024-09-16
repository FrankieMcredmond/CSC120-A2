from typing import Dict, Optional
from computer import Computer
class ResaleShop:

    # What attributes will it need?
    inventory : dict[int, dict] = {}
    item_id: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, ):
        self.inventory= inventory
        self.item_id=0
    # What methods will you need?
        #buy computer
        #selling a computer
        #refurbishing a computer
    def buy(self, computer):
        self.inventory.append (computer)
        self.item_id+= 1
        print (self.item_id)
    def sell(self, item_id ):
        self.inventory.remove (item_id)
        print ("Item sold", self.item_id)

def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500,)
    computer_2 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500,)
    print (computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price)
    computer.update_price(50)
    resaleshop= ResaleShop ([])
    resaleshop.buy(computer)
    resaleshop.buy(computer_2)

if __name__ == "__main__":
    main()