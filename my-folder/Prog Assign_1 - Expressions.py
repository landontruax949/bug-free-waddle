equation = int(input( "What kind of equation do you want to solve? (1 = addition, 2 = subtraction, 3 = multiplication, 4 = division)"))
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
if equation == 1:
    total = num1 + num2
elif equation == 2:
    total = num1 - num2
elif equation == 3:
    total = num1 * num2
elif equation == 4:
    total = num1 / num2
print("The total is ", total)

input("Press enter to exit")