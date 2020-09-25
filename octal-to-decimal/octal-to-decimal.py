import re

def getInput():
    octalRegex = re.compile(r'[^0-7.]').search

    octalString = ""
    while True:
        octalString = input("Enter an octal number: ")

        if not octalRegex(octalString): break
        else: print("Please enter a valid octal number!")

    return octalString

def getDecimalBeforePoint(octalBeforePoint):
    octalLen = len(octalBeforePoint)

    decimalTemp = 0
    for i in range(octalLen-1, -1, -1):
        decimalTemp += int(octalBeforePoint[i]) * (8**(octalLen-i-1))

    return decimalTemp

def getDecimalAfterPoint(octalAfterPoint):
    octalLen = len(octalAfterPoint)

    decimalTemp = 0
    for i in range(octalLen):
        decimalTemp += int(octalAfterPoint[i]) * (8**(-(i+1)))

    return decimalTemp

print("Octal to Decimal Converter by Marcellino Chris O\'Vara")
print("----------------------------------------------")
print("Enter a octal number without preceding \'0o\'!")
print("Press enter to exit!")
print("----------------------------------------------")
while True:
    octal = getInput()
    if octal == "":
        print("Exit!")
        break

    decimal = 0

    octalSplit = octal.split('.')
    decimal += getDecimalBeforePoint(octalSplit[0])
    if len(octalSplit) >= 2:
        decimal += getDecimalAfterPoint(octalSplit[1])

    print(decimal)
