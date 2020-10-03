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

def getOctalBeforePoint(decimal):
    if decimal < 8: return str(decimal)

    return getOctalBeforePoint(decimal//8) + str(decimal % 8)

def getOctalAfterPoint(decimal, roundTo):
    if roundTo == 0 or decimal == 0.0:
        return ""

    return str(int(decimal*8)) + getOctalAfterPoint(decimal*8 - int(decimal*8), roundTo-1)

print("Decimal to Octal Converter by Marcellino Chris O\'Vara")
print("----------------------------------------------")
print("Enter a decimal number!")
print("Press enter to exit!")
print("----------------------------------------------")
while True:
    decimal = getInput()
    if decimal == "":
        print("Exit!")
        break

    octal = ""

    decimalSplit = decimal.split('.')
    octal += getOctalBeforePoint(int(decimalSplit[0]))
    if len(decimalSplit) >= 2:
        roundTo = getRoundTo()
        if roundTo == "":
            print("Exit!")
            break
        octal += '.' + getOctalAfterPoint(float('0.' + decimalSplit[1]), int(roundTo))
        

    print(octal)
