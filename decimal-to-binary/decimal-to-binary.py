import re

def getInput():
    decimalRegex = re.compile(r'[^0-9.]').search

    decimalString = ""
    while True:
        decimalString = input("Enter a decimal number: ")

        if not decimalRegex(decimalString): break
        else: print("Please enter a valid decimal number!")

    return decimalString

def getRoundTo():
    roundToRegex = re.compile(r'[^0-9]').search

    roundToString = ""
    while True:
        roundToString = input("Round the result to: ")

        if not roundToRegex(roundToString): break
        else: print("Please enter an integer!")

    return roundToString

def getBinaryBeforePoint(decimal):
    if decimal == 0: return "0"
    elif decimal == 1: return "1"

    return getBinaryBeforePoint(decimal//2) + str(decimal % 2)

def getBinaryAfterPoint(decimal, roundTo):
    if roundTo == 0 or decimal == 0.0:
        return ""

    return str(int(decimal*2)) + getBinaryAfterPoint(decimal*2 % 1, roundTo-1)

print("Decimal to Binary Converter by Marcellino Chris O\'Vara")
print("----------------------------------------------")
print("Enter a decimal number!")
print("Press enter to exit!")
print("----------------------------------------------")
while True:
    decimal = getInput()
    if decimal == "":
        print("Exit!")
        break
    
    binary = ""

    decimalSplit = decimal.split('.')
    binary += getBinaryBeforePoint(int(decimalSplit[0]))
    if len(decimalSplit) >= 2:
        roundTo = getRoundTo()
        if roundTo == "":
            print("Exit!")
            break
        binary += '.' + getBinaryAfterPoint(float('0.' + decimalSplit[1]), int(roundTo))

    print(binary)
