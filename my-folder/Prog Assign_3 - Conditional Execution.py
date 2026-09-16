# rewrote a lot of code from assign_1, changed to display a specific value instead of calculating numbers
day = int(input("Pick a number corresponding to a day of the week (1-7). "))

if day == 1:
    total = "Monday"
elif day == 2:
    total = "Tuesday"
elif day == 3:
    total = "Wednesday"
elif day == 4:
    total = "Thursday"
elif day == 5:
    total = "Friday"
elif day == 6:
    total = "Saturday"
elif day == 7:
    total = "Sunday"
else: total = "invalid"
# the "else:" line is used as a failsafe because it will only trigger if the user inputs a value outside of the accepted range

# before printing the day, the code will check if the input was valid
if total == "invalid":
    print("Invalid number.")
else: print("The day is", total)

input("Press enter to exit")