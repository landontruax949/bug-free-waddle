ABC = '2'
DEF = '3'
GHI = '4'
JKL = '5'
MNO = '6'
PQRS = '7'
TUV = '8'
WXYZ = '9'
# each value represents a different set of letters that correspond to the same number

phone = (input("Type a 10-digit long telephone number in the format XXX-XXX-XXXX. Words can be used. "))
# the user is asked to input a phone number. an example could be 302-ABC-DEFG.

translated = ""

for character in phone:
    letter = character.upper()

    if letter in "ABC":
        translated += str(ABC)
    elif letter in "DEF":
        translated += str(DEF)
    elif letter in "GHI":
        translated += str(GHI)
    elif letter in "JKL":
        translated += str(JKL)
    elif letter in "MNO":
        translated += str(MNO)
    elif letter in "PQRS":
        translated += str(PQRS)
    elif letter in "TUV":
        translated += str(TUV)
    elif letter in "WXYZ":
        translated += str(WXYZ)
    else:
        translated += character
# "letter in "ABC": " means that the code will check if the letter is A, B, or C.
# if it is, then the code will check what the string ABC equals and add it to the translation. this is repeated for every other set of letters.

print("The phone number is", translated)

input("Press enter to exit.")