print("""Welcome to montly phone payment evaluator.\n To exit enter "exit" """)
while True:
    try:
        minutes = input("Enter the duration in minutes of phonecalls with users of other operators over the month : ")
    except:
        break

    if minutes == "exit":
        break

    try:
        minutes = int(minutes)
    except:
        print("Please enter the value that consists of numbers [0-9]")
        continue
    
    if minutes < 0:
        print("Duration must be a non negative value")
        continue

    total = 100
    if minutes > 50:
        total += 50
        minutes -= 100
        if minutes > 0:
            total += minutes * 2

    print(f"Your total paycheck for the phonecalls for month will be {total} hryvnas")
