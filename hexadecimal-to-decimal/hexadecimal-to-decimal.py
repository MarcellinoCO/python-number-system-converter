import re

hdDigits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

def getInput():
    hdRegex = re.compile(r'[^0-9a-fA-F.]').search

    hdString = ""
    while True:
        hdString = input("Enter a hexadecimal number: ")

        if not hdRegex(hdString): break
        else: print("Please enter a valid hexadecimal number!")

    return hdString.upper()

def getDecimalBeforePoint(hdBeforePoint):
    hdLen = len(hdBeforePoint)

    decimalTemp = 0
    for i in range(hdLen-1, -1, -1):
        decimalTemp += hdDigits[hdBeforePoint[i]] * (16**(hdLen-i-1))

    return decimalTemp

def getDecimalAfterPoint(hdAfterPoint):
    hdLen = len(hdAfterPoint)

    decimalTemp = 0
    for i in range(hdLen):
        decimalTemp += hdDigits[hdAfterPoint[i]] * (16**(-(i+1)))

    return decimalTemp

print("Hexadecimal to Decimal Converter by Marcellino Chris O\'Vara")
print("----------------------------------------------")
print("Enter a hexadecimal number without preceding \'0x\'!")
print("Press enter to exit!")
print("----------------------------------------------")
while True:
    hd = getInput()
    if hd == "":
        print("Exit!")
        break

    decimal = 0

    hdSplit = hd.split('.')
    decimal += getDecimalBeforePoint(hdSplit[0])
    if len(hdSplit) >= 2:
        decimal += getDecimalAfterPoint(hdSplit[1])

    print(decimal)
