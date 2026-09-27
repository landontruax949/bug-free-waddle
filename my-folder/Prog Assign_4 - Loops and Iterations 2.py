total = 0
months = 0
average = 0
# the starting amount of rainfall, months, and the average amount of rainfall
years = int(input("How many years?"))
# the user determines how many times the outer loop should run for

for i in range(years): 
    # the nested loop runs 12 times for each year (ex. 3 years = 36 loops.)
    for i in range(12):
        rain = int(input("How many inches of rain fell this month? "))
        total += rain
        months += 1
        # same thing as program 1, just with the addition of months
        average = total / months
        # dividing the total inches of rainfall by the amount of months will give the average amount of rainfall
else: print(total, "inches of rain fell over the course of", months, "month(s), or", years, "year(s).", "The average amount of rain per month was", average, "inches.")