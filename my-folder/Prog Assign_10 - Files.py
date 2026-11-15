file = input("Input the name of a file.")

with open(file, "r") as infile:
    contents = infile.readlines()[:5]

print("".join(contents))
infile.close()
input("Press enter to exit.")