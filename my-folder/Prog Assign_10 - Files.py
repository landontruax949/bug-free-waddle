from pathlib import Path
file = input("Enter the name of a file: ")

file_path = Path(__file__).with_name(file)
with file_path.open("r") as file:
    contents = file.readlines()[:5]
print("".join(contents))

input("Press enter to exit.")