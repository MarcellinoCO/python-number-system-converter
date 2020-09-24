import re

def getInput():
    binaryRegex = re.compile(r'[^0-1.]').search

    binaryString = ""
    while True:
        binaryString = input("Enter a binary number: ")

        if not binaryRegex(binaryString): break
        else: print("Please enter a valid binary number!")

    return binaryString

def getDecimalBeforePoint(binaryBeforePoint):
    binaryLen = len(binaryBeforePoint)

    decimalTemp = 0
    for i in range(binaryLen-1, -1, -1):
        decimalTemp += int(binaryBeforePoint[i]) * (2**(binaryLen-i-1))

    return decimalTemp

def getDecimalAfterPoint(binaryAfterPoint):
    binaryLen = len(binaryAfterPoint)

    decimalTemp = 0
    for i in range(binaryLen):
        decimalTemp += int(binaryAfterPoint[i]) * (2**(-(i+1)))

    return decimalTemp

print("Binary to Decimal Converter by Marcellino Chris O\'Vara")
print("----------------------------------------------")
print("Enter a binary number without preceding \'0b\'!")
print("Press enter to exit!")
print("----------------------------------------------")
while True:
    binary = getInput()
    if binary == "":
        print("Exit!")
        break

    decimal = 0

    binarySplit = binary.split('.')
    decimal += getDecimalBeforePoint(binarySplit[0])
    if len(binarySplit) >= 2:
        decimal += getDecimalAfterPoint(binarySplit[1])

    print(decimal)
