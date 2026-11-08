import random
# allows the code to randomize the questions

capitals = {
 "Washington": "Olympia",
 "Oregon": "Salem",
 "California": "Sacramento",
 "Nevada": "Carson City",
 "Idaho": "Boise",
 "Montana": "Helena",
 "Wyoming": "Cheyenne",
 "Utah": "Salt Lake City",
 "Colorado": "Denver",
 "New Mexico": "Santa Fe",
 "Arizona": "Phoenix",
 "Hawaii": "Honolulu",
 "Alaska": "Juneau",
 "North Dakota": "Bismarck", 
 "South Dakota": "Pierre",
 "Nebraska": "Lincoln",
 "Kansas": "Topeka",
 "Oklahoma": "Oklahoma City",
 "Texas": "Austin",
 "Minnesota": "St. Paul",
 "Iowa": "Des Moines",
 "Missouri": "Jefferson City",
 "Arkansas": "Little Rock",
 "Louisiana": "Baton Rouge",
 "Wisconsin": "Madison",
 "Illinois": "Springfield",
 "Mississippi": "Jackson",
 "Michigan": "Lansing",
 "Indiana": "Indianapolis",
 "Ohio": "Columbus",
 "Kentucky": "Frankfort",
 "Tennessee": "Nashville",
 "Alabama": "Montgomery",
 "Georgia": "Atlanta",
 "Florida": "Tallahassee",
 "North Carolina": "Raleigh",
 "South Carolina": "Columbia",
 "Virginia": "Richmond",
 "West Virginia": "Charleston",
 "New York": "Albany",
 "Pennsylvania": "Harrisburg",
 "Maryland": "Annapolis",
 "New Jersey": "Trenton",
 "Connecticut": "Hartford",
 "Vermont": "Montpelier",
 "New Hampshire": "Concord",
 "Maine": "Augusta",
 "Rhode Island": "Providence",
 "Massachusetts": "Boston",
 "New Jersey": "Trenton",
 "Delaware": "Dover",

}
correct = 0
incorrect = 0

for i in range(10):
    state = random.choice(list(capitals.keys))
# state will be randomly selected from the list above
question = input("What is the capital of ", {state}, "?")
answer = capitals[state]

if question == answer:
    print("Correct!")
    correct += 1
else:
    print("Incorrect.")
    incorrect += 1

print("You got", correct, "correct and", incorrect, "incorrect.")