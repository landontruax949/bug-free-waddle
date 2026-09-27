total = 0
# the starting number of bugs

for i in range(5):
    bugs = int (input("How many bugs were caught in a day? "))
    # the loop asks the user to input a number that represents the amount of bugs a total of five times
    total += bugs
    # "total += bugs" adds the inputted amount of bugs to the total number of bugs
else: print(total, "bugs were caught over five days.")

input("Press enter to exit.")