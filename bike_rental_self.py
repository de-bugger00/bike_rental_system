#------------------------------------------------------ Bike Rental system ------------------------------------------------------#

class bikes:
    def __init__(self,bike,display,hour):
        self.master = display.copy()
        self.display = display
        self.bike = bike.lower()
        self.hour = hour
        self.deposite = []
        self.bikes_left = display

    def calculate_charges(self):
        charges_after_subb=(display[self.bike.lower()]) * self.hour
        return(charges_after_subb)
        # print(charges_after_subb)
    
    def display_bike(self):
        display.pop(self.bike.lower())
        if len(self.display) == 0:
            return("No bikes left for rental")
        else:
            return(self.display)
    
    def deposite_bike(self, deposite):
        display[deposite]=self.master[deposite]
        "self.display.get(deposite) ",self.master
        return self.display
    
    def menu(self):
        while True:
            print("""
                    Bike Rental Menu
                ************************
                    Menu:
                    1. Rent a bike.
                    2. Deposite a bike.
                    3. Check bike availability.
                    4. Exit
                ************************
                """)
            # while True:
            try:
                option = int(input("Enter 1,2,3 or 4"))
            except:
                print("Error: Enter 1,2,3 or 4 only\n")
                continue
            else:
                    if option == 1:
                        self.bike = input("Enter the name of the bike: ")
                        try:
                            self.hour = float(input("Enter the hours for you want to use bike: "))
                        except:
                            print("Hours should be in numeric value only.\n")
                            continue
                        if self.bike.lower() in display:
                            # print(display)
                            total_charge = self.calculate_charges()
                            self.display_bike()
                            print("The bike selected is {} and the total rental amount for {} hours is Rs {}".format(self.bike,self.hour,total_charge))
                            # print(display)
                        else:
                            print("The the bike {} is not available for rent. Please select the bikes available in display.".format(self.bike))
                        # break
                    elif option == 2:
                        deposite = input("Enter a name of bike you want to return: ")
                        if deposite.lower() in self.display:
                            print("The bike is already in stock you cannot deposite before renting it.")
                        if deposite.lower() not in self.display and deposite.lower() in self.master:
                                depo = self.deposite_bike(deposite.lower())
                                print("The bike {} is deposited.".format(deposite.lower()))
                                print("The current bikes available is {}".format(depo))
                        if deposite.lower() not in self.master:
                            print("Kindly enter the correct bike name.")
                        # break
                    elif option == 3:
                        # bikes_left = self.display_bike()
                        print(self.display)
                        # break
                    elif option == 4:
                        print("Thanks for visiting")
                        break


display = {"yamaha":100,"hero":80,"bajaj":70}
print(display)
bike=''
hour=''
# bike = input("Enter the name of the bike: ")
# hour = int(input("Enter the hours for you want to use bike: "))
# obj = bikes(bike,display,hour)
obj=bikes(bike,display,hour)

# deposite = {"Yamaha":100,"Hero":80,"Bajaj":70}
while True:
    choice = input("Do you want to rent/deposite a bike? (y/n): ")
    if choice == "y":
        obj.menu()
    elif choice == "n":
        print("""
         ---------------------------------------
        | Thanks for choosing us to rent a bike |
         ---------------------------------------
        """)
        break
    else:
        print("Wrong command: Enter 'y' for Yes and 'n' for No\n" )