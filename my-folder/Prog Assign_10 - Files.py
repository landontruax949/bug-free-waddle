file = input("Input the name of a file: ")

try:
    with open(file, "r") as infile:
        contents = infile.readlines()[:5]
    print("".join(contents))
except FileNotFoundError:
    print("File not found.")
infile.close()

input("Press enter to exit.")