from pathlib import Path
# path is needed to help find the file
file = input("Enter the name of a file: ")
# user is asked to input the exact name of a file
file_path = Path(__file__).with_name(file)
# program searches for a file with the inputted name inside this file's current path 
with file_path.open("r") as file:
    contents = file.readlines()[:5]
# the found file is opened and has its first five lines read
print("".join(contents))
# the five lines are joined into a single output
input("Press enter to exit.")