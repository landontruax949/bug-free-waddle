numbers = [int(value.strip()) for value in input("Type a list of numbers, separated by commas (Do not include a period.): ").split(",")]
# the user is asked to input a list of numbers seperated by commas (ex. 2, 4, 19, 23).

print("Total:", sum(numbers))
print("Highest:", max(numbers))
# the code checks for the total amount of numbers and the highest amongst them and prints it out

average = sum(numbers)/len(numbers)
# equation to check for the average, which is done by dividing the sum by the amount
print("Average:", average)

input("Press enter to exit.")