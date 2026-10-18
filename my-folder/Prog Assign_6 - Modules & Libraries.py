paintperhour = 0.125
feetperhour = 14
priceperhour = 35.00
#i tried importing a module containing this data (called Paint) but could not get it to fully work.
#i might've been trying to use a module incorrectly but i'm still not too sure on how they exactly work.

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