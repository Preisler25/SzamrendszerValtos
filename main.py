import math

def convertFromDecToHex(num):
    numMap = dict()

    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for i in range(len(list)):
        numMap[i] = list[i]

    tempValue = ""
    i = int(num)
    while i / 16 >= 1:
        tempValue += f"{numMap[i%16]}"
        i = math.floor(i/16)
    tempValue += f"{i}"
    return tempValue[::-1]

def convertFromDecToBin(num):
    tempValue = ""
    i = int(num)
    while i != 0:
        if i % 2 == 1:
            tempValue += "1"
        else:
            tempValue += "0"
        i = math.floor(i/2)
    return tempValue[::-1]

def convertFromHexToDec(num):
    numMap = dict()

    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for i in range(len(list)):
        numMap[list[i]] = i

    tempValue = 0
    temp_power = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] != "0":
            tempValue += (numMap[num[i]] * math.pow(16, temp_power))
        temp_power += 1 
    return tempValue

def convertFromBinToDec(num):
    tempValue = 0
    temp_power = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] != "0":
            tempValue += math.pow(2, temp_power)
        temp_power += 1 
    return tempValue

def userInput():
    value = input("Kérlek adj meg egy számots:")
    match value[0:2]:
        case "0b":
            print(f"A szám 10-es számrendszerben: {convertFromBinToDec(value[2:])}\nA szám 16-os számrendszerben: {convertFromDecToHex(convertFromBinToDec(value[2:]))} ")
        case "0x":
            print(f"A szám 10-es számrendszerben: {convertFromHexToDec(value[2:])}\nA szám 2-es számrendszerben: {convertFromDecToBin(convertFromHexToDec(value[2:]))}")
        case "0d":
            print(f"A szám 16-os számrendszerben: {convertFromDecToHex(value[2:])}\nA szám 2-es számrendszerben: {convertFromDecToBin(value[2:])}")
    print("------------------------------------------------------------------------------------")

def main():
    while True:
        userInput()


main()


        
            