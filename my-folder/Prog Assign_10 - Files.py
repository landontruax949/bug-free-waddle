try:
    with open("Prog Assign_1 - Expressions.py", "r") as infile:
        contents = infile.readlines()[:5]
    print("".join(contents))
except FileNotFoundError:
    print("File not found.")

input("Press enter to exit.")