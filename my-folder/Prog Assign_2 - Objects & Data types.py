class Car:
    def __init__(self, speed):
        self.speed = speed
p1 = Car(70)

# reused some code from the previous assignment to allow the user to decide how long the car drives for (in hours)
time = int(input("How many hours does the car drive for? "))

distance = p1.speed * time

print("In", time, "hours, the car will travel", distance, "miles.")

input("Press enter to exit")