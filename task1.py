import math


def readFloat(prompt):
    s_input = ''
    f_value = 0
    while True:
        try:
            s_input = input(prompt)
        except KeyboardInterrupt:
            return "exit"
        if s_input == "exit":
            return "exit"

        try:
            f_value = float(s_input)
        except Exception:
            print("Value is not float")
            continue
        if f_value <= 0:
            print("Value must be positive")
            continue

        return f_value


def check():
    print("To quit the program enter 'exit'")
    a = readFloat("Enter length of triangle side a: ")
    if a == "exit":
        return None
    b = readFloat("Enter length of triangle side b: ")
    if b == "exit":
        return None
    c = readFloat("Enter length of triangle side c: ")
    if c == "exit":
        return None

    return (a, b, c)


def triangle_ineq(func):
    def triangle_ineq_check(a, b, c):
        if c < a+b and b < a+c and a < b+c:
            print(f"Area of entered triangle is {func(a,b,c)} square units")
        else:
            print("Entered sides can not form a triangle.")
    return triangle_ineq_check


@triangle_ineq
def area_calculation(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p * (p-a)*(p-b)*(p-c))


res = check()
if res is not None:
    area_calculation(*res)
