file = int(input("Input the name of a file."))

infile = open(file)
contents = infile.readlines(1,5)

print(contents)

input("Press enter to exit.")