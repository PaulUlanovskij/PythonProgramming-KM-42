import numpy as np

years = np.arange(1900, 2020+5, 1)

def readInt(prompt):
    s_input = ''
    while True:
        try:
            s_input = input(prompt)
        except KeyboardInterrupt:
            return "exit"
        if s_input == "exit":
            return "exit"
        try:
            i_value = int(s_input)
            return i_value
        except ValueError:
            print("Please enter the number consiting digits [0-9]")


def readYear():
    i_year = 0
    while True:
        i_year = readInt("Please enter the year: ")
        if i_year == "exit":
            return "exit"
        if i_year >= 1900 and i_year < 2025:
            return i_year
        print("Error: Years sould be in bound [1900 - 2024]")


def readMonth():
    i_month = 0
    while True:
        i_month = readInt("Please enter the month: ")
        if i_month == "exit":
            return "exit"
        if i_month >= 1 and i_month < 13:
            return i_month
        print("Error: Month sould be in bound [1 - 12]")


def isLeap(list_years):
    return list(map(int, list(filter(lambda y: y % 400 == 0 or (not y % 400 == 0 and not y % 100 == 0 and y % 4 == 0), list_years))))


def getDays(year, month, leap_years_generator):
    b_isLeap = year in leap_years_generator(years)
    
    match month:
        case 1 | 4 | 6 | 9 | 11: print(30)
        case 2: print(29 if b_isLeap else 28)
        case 3 | 5 | 7 | 8 | 10 | 12: print(31)


while True:
    print("Enter 'exit' to exit the program")
    i_year = readYear()
    if i_year == "exit":
        break
    i_month = readMonth()
    if i_month == "exit":
        break
    getDays(i_year, i_month, isLeap)
