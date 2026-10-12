#the program starts by asking the user to list off their monthly expenses
loan = int(input("How much do you pay on car loans monthly? "))
insurance = int(input("How much do you spend on car insurance monthly? "))
gas = int(input("How much does gas cost you monthly? "))
oil = int(input("How much does oil cost you monthly? "))
tires = int(input("How much do you pay for tires monthly? "))
maintenance = int(input("How much do you pay for maintenance this month? "))

#the function "monthly()" combines the expenses into a single cost
def monthly():
    return loan + insurance + gas + oil + tires + maintenance

#the function "annually()" multiplies the expenses by 12 to simulate how much they would cost in a year.
def annually():
    return (monthly() * 12)

print("You spend", monthly(), "on your car monthly, and will spend", annually(),"annually.")

input ("Press enter to exit.")