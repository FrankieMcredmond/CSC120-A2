class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    #item_id: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, description: str, processor_type: str , hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int ):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price
    def update_price(self, new_price):
        self.price=new_price
        print ("updated price", self.price)
    def update_OS(self, new_operatingsystem):
        self.operating_system=new_operatingsystem
        print ("updated OS", self.operating_system)

        
    

    # What methods will you need?
   # main
    #update price
   # update OS

def main():
    
    # First, let's make a computer
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500,)
    print (computer.description, computer.processor_type, computer.hard_drive_capacity, computer.memory, computer.operating_system, computer.year_made, computer.price)
    computer.update_price(50)
    computer.update_OS("small sur")
# only call main if running directly
if __name__ == "__main__":
    main()