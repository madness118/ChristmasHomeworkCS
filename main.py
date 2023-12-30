import random

Days = [1, 2, 3, 4, 5, 6, 7]
Readings = [[round(random.uniform(-20.00, 50.00), 2) for j in range(24)] for i in range(7)] #fills array so its not all 0s
AverageTemp = []

#works
def CtoF(temp): #function to convert celcius to fahrenheit
    return round(temp * 9/5 + 32, 2)

def choosing(message, min, max, datatype=int):
        while True:
            try:
                while True:
                    var = datatype(input(message))
                    if min <= var <= max:
                        break
                    else:
                        print("Value cannot be accepted")
                break
            except TypeError:
                print("Please enter an integer")
                continue
            except ValueError:
                print("Please enter an integer")
                continue
        return var


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
    choice = choosing("Choose Action:\n\n1. Input temperatures\n2. Show daily average\n3. Show weekly average\n4. Show temperature\n5. Show all temperatures\n6. Leave\n\n", 1, 6)
    return choice    

#works
def inputTemp(): 
    day = choosing("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n", 1, 7)
    print(f"Day: {chooseDay(day)}")
    hour = choosing("Enter an hour (1-24): ", 1, 24)
    temp = choosing("Enter temperature: ", -20.00, 50.00, float)
    Readings[day][hour] = round(temp, 2)
    print(f"Updated hour {hour} of {chooseDay(day)}\n")
    updateAvgTemp()


def dailyAvg():
    day = choosing("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n", 1, 7)
    version = choosing("1. Celcius\n2. Fahrenheit\n\n", 1, 2)
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
    version = choosing("1. Celcius\n2. Fahrenheit\n\n", 0, 3)
    avg = round(Total/Counter, 2)
    if version == 1:
        print(f"Average temperature for the week in Celcius: {avg}\n")
    else:
        print(f"Average temperature for the week in Fahrenheit: {CtoF(avg)}\n")

def showTemp():
    day = choosing("Choose a day:\n\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n\n", 1, 7)
    print(f"Day: {chooseDay(day)}")
    hourIndex = choosing("Enter an hour (1-24): ", 1, 24)
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