import math


def readFloat(prompt):
    while True:
        s_input = ''
        try:
            s_input = input(prompt)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt. Exiting...")
            return "exit"
        if s_input == "exit":
            return "exit"

        f_value = 0

        try:
            f_value = float(s_input)
        except ValueError as ve:
            print(ve)
            print("Please reenter the value matching pattern [0-9]+\\.[0-9]+")
            continue
        return f_value


f_A = 0
f_B = 0
f_C = 0
# Equasion is solved by Po-Shen Loh Method
while True:
    print("Enter quotients of quadratic equasion to solve. To exit enter 'exit'")
    f_A = readFloat("Enter quotient a that is multiplied by x^2: ")
    if f_A == "exit":
        break
    f_B = readFloat("Enter quotient b that is multiplied by x: ")
    if f_B == "exit":
        break
    f_C = readFloat("Enter free quotient c: ")
    if f_C == "exit":
        break

    try:
        f_B /= f_A
        f_C /= f_A
        f_A /= f_A
    except ZeroDivisionError as de:
        print(de)
        print("This implies that equasion has one or no roots")
        try:
            f_x = -f_C/f_B
        except ZeroDivisionError as de1:
            print(de1)
            print("Equasion has no roots")
        else:
            print(f"Equasion has one root x: {f_x}")

    else:
        f_midpoint = -f_B/2*f_A
        f_u = f_midpoint * f_midpoint - f_C

        try:
            f_u = math.sqrt(f_u)
        except ValueError as ve:
            print(ve)
            print("Attempted to take a square root of a negative number.\nThis implies that equasion has no roots")
        else:
            f_x1 = f_midpoint - f_u
            f_x2 = f_midpoint + f_u

            if f_x1 == f_x2:
                print(f"Root of equasion is x: {f_x1}")
            else:
                print(f"Roots of equasion are x1: {f_x1} and x2: {f_x2}")
    print()
