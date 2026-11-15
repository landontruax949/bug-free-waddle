from pathlib import Path

file_path = Path(__file__).with_name("Prog Assign_1 - Expressions.py")
with file_path.open("r") as file:
    contents = file.readlines()[:5]
print("".join(contents))

input("Press enter to exit.")