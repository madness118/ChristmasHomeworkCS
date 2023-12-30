import random

Days = [1, 2, 3, 4, 5, 6, 7]
Readings = [[round(random.uniform(-20.00, 50.00), 2) for j in range(24)] for i in range(7)] #fills array so its not all 0s
AverageTemp = []

#works
def CtoF(temp): #function to convert celcius to fahrenheit
    return round(temp * 9/5 + 32, 2)

#works
def updateAvgTemp():
    Total = 0
    for n in range(len(Readings)):
        for i in range(len(Readings[n])):
            Total += Readings[n][i]
        Average = round(Total/24, 2)
        Total = 0
        AverageTemp.append(Average)

updateAvgTemp()

#works
def chooseDay(num): #converts numbers to days
    match num:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5: 
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'

def menu():
    while True:
        choice = int(input("Choose Action:\n\n1. Input temperatures\n2. Show daily average\n3. Show weekly average\n4. Show temperature\n5. Show all temperatures\n6. Leave\n\n"))
        if choice > 0 and choice < 7:
            return choice
        else:
            print("Not a valid option")
        

#works
def inputTemp(): 
    while True:
        day = int(input("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n"))
        if day >= 1 and day <= 7:
            break
    print(f"Day: {chooseDay(day)}")
    while True:
        hour = int(input("Enter an hour (1-24): "))
        if hour > 0 and hour < 25:
            break
    while True:
        temp = float(input("Enter temperature: "))
        if temp > -20.00 and temp < 50.00:
            break
        else:
            print("Value out of range")
    Readings[day][hour] = round(temp, 2)
    print(f"Updated hour {hour} of {chooseDay(day)}\n")
    updateAvgTemp()


def dailyAvg():
    while True:
        day = int(input("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n"))
        if day >= 1 and day <= 7:
            break
    while True:
        version = int(input("1. Celcius\n2. Fahrenheit\n\n"))
        if version > 0 and version < 3:
            break
        else:
            print("Not a valid option")
    if version == 1:
        print(f"Average temperaure of {chooseDay(day)} in Celcius: {AverageTemp[day]}\n")
    else:
        print(f"Average temperaure of {chooseDay(day)} in Fahrenheit: {CtoF(AverageTemp[day])}\n")

def weeklyAvg():
    Total = 0
    Counter = 0
    for i in range(len(Readings)):
        for j in range(len(Readings[i])):
            Total += Readings[i][j]
            Counter += 1
    while True:
        version = int(input("1. Celcius\n2. Fahrenheit\n\n"))
        if version > 0 and version < 3:
            break
        else:
            print("Not a valid option")
    avg = round(Total/Counter, 2)
    if version == 1:
        print(f"Average temperature for the week in Celcius: {avg}\n")
    else:
        print(f"Average temperature for the week in Fahrenheit: {CtoF(avg)}\n")

def showTemp():
    while True:
        day = int(input("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n"))
        if day >= 1 and day <= 7:
            break
    print(f"Day: {chooseDay(day)}")
    while True:
        hourIndex = int(input("Enter an hour (1-24): "))
        if hourIndex > 0 and hourIndex < 25:
            break
    temp = Readings[day][hourIndex]
    print(f"Temperature at {hourIndex}:00 on {chooseDay(day)}\nCelcius: {temp}\nFahrenheit: {CtoF(temp)}")

def showAllTemp():
    for i in range(len(Readings)):
        print(f"{chooseDay(i)}: {Readings[i]}")
    print()

while True:
    match menu():
        case 1:
            inputTemp()
        case 2:
            dailyAvg()
        case 3:
            weeklyAvg()
        case 4:
            showTemp()
        case 5:
            showAllTemp()
        case 6:
            break

