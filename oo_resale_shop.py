from typing import Dict, Optional
from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory= list
    item_id_counter: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory= []
        self.item_id_counter=0
    # What methods will you need?
        #buy computer
        #selling a computer
        #refurbishing a computer
    def buy(self, computer):
        self.item_id_counter+= 1
        computer.item_id= self.item_id_counter
        self.inventory.append (computer)
    def sell(self, computer):
        self.inventory.remove (computer)
        print ("Item sold", computer.item_id)

def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500,)
    computer.update_price(50)
    myShop: ResaleShop= ResaleShop()
    print("Inventory b4 buying", len(myShop.inventory))
    myShop.buy(computer)
    print("Inventory after buying", len(myShop.inventory))
    myShop.sell(computer)
    print("Inventory after selling", len(myShop.inventory))
    
if __name__ == "__main__":
    main()