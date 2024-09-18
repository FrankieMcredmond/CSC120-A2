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
        print("Inventory after buying item: ", len(self.inventory), "\n")

    def sell(self, computer):
        print("selling ", computer.description, "...")
        if computer in self.inventory:
            self.inventory.remove (computer)
            print ("Item sold: ", computer.description)
        else:
            print("sorrrrryyyyyy not in inventory \n")

    def print_inventory(self):
        print("printing inventory...")
        for i in self.inventory:
            print (f'Item : {i.description} : DESCRIPTION {i.description} PROCESSOR {i.processor_type} HARD DRIVE CAPACITY {i.hard_drive_capacity} MEMORY {i.memory} OPERATING SYSTEM {i.operating_system} YEAR MADE {i.year_made} PRICE {i.price} ID {i.item_id}')
        if self.inventory==[]:
            print ("Sorry, no items in inventory :(")
        print ('\n')

            
    def refurbish (self, computer, new_os):
        print("Refurbishing",  computer.description, "...")
        if computer in self.inventory:
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
            print("Item not found in inventory :(\n")
            

def main():
    print("\nWelcome to the Computer Store! :)") #Welcome Message
    new_os= "Mac OS monterey" #establishes most recent OS
    computer = Computer("Mac Pro (Late 2008)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2008, 1500) #Creates computer
    computer_2 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Monterey", 2013, 1500) #creates  2nd Computer
    myShop: ResaleShop= ResaleShop() #creates shop
    print("Inventory before buying items: ", len(myShop.inventory), "\n") 
    myShop.print_inventory() #error test
    myShop.refurbish(computer,new_os) # error test
    myShop.sell(computer) #error test
    myShop.buy(computer)
    myShop.buy(computer_2)
    myShop.refurbish(computer,new_os)
    myShop.print_inventory()
    myShop.sell(computer)
    print("Inventory after selling item:", len(myShop.inventory))
    
if __name__ == "__main__":
    main()