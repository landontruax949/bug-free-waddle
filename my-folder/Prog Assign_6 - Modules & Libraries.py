import Paint
#contains data about the rates of the paint company

squarefeet = int(input( "How much area needs to be painted? (in square feet.) "))
paintprice = int(input( "How much does a single gallon of paint cost? (in dollars rounded up.) "))

hours = squarefeet/feetperhour
gallons = paintperhour * hours
galloncost = gallons * paintprice 
cost = priceperhour * hours
totalcost = cost + galloncost
# determines the number of hours and then uses that to calculate the gallons of paint and cost of labor 

print("The job will take", hours,"hour(s) and will require", gallons,"gallon(s) of paint. The labor cost will be", cost,"dollars, and it will cost around", galloncost,"dollars for enough paint. The total cost of the job is", totalcost,"dollars.")
#displays all of the calculated values
input ("Press enter to exit.")