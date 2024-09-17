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
        print ("Item bought: ", computer.description)

    def sell(self, computer):
        print("selling ", computer.description, "...")
        if computer in self.inventory:
            self.inventory.remove (computer)
            print ("Item sold: ", computer.description)
        else:
            print("sorrrrryyyyyy no computer")

    def print_inventory(self):
        print("printing inventory...")
        for computer in self.inventory:
            print (f'Item ID: {computer.item_id} : {computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price}\n')
   
    def refurbish (self, computer, new_os):
        if computer in self.inventory:
            print("Refurbishing",  computer.description, "...")
            if computer.year_made<= 2000:
                computer.update_price(0)
                if computer.operating_system!=new_os:
                    computer.update_OS(new_os)
            elif computer.year_made<= 2012:
                computer.update_price(250)
                if computer.operating_system!=new_os:
                    computer.update_OS(new_os)
            elif computer.year_made<= 2018:
                computer.update_price(550)
                if computer.operating_system!=new_os:
                    computer.update_OS(new_os)
            else:
                computer.update_price(1000)
                if computer.operating_system!=new_os:
                    computer.update_OS(new_os)
            print("Done!\n")
        else:
            print("Item not found in inventory :(")
            

def main():
    print("\nWelcome to the Computer Store! :)")
    new_os= "Mac OS monterey"
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500,)
    myShop: ResaleShop= ResaleShop()
    print("Inventory before buying items: ", len(myShop.inventory), "\n")
    myShop.buy(computer)
    print("Inventory after buying item: ", len(myShop.inventory), "\n")
    myShop.refurbish(computer,new_os)
    myShop.print_inventory()
    myShop.sell(computer)
    print("Inventory after selling item:", len(myShop.inventory))
    
if __name__ == "__main__":
    main()