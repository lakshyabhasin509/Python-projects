print("Welcome to tip calculator")
bill=float(input("What is the Total bill?\n"))
people=int(input("How many people would you like to split the bill\n"))
rate=int(input("What percentage tip you want to give? 10,12 or 15\n"))

totalbill =bill+(rate/100)*bill


print("Each person should pay " + str(int(totalbill/people)))