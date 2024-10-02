print("""Welcome to rating to grade converter.\n To exit write "exit" """)
while True:
    try:
        grade = input("Enter the rating grade : ")
    except:
        break

    if grade == "exit":
        break

    try:
        grade = int(grade)
    except:
        print("Please enter the value that consists of numbers [0-9]")
        continue
    
    if grade < 0 or grade > 100:
        print("Rating grade must be in range [0-100]")
        continue

    if grade >= 95:
        print("Excellent")
    elif grade >= 85:
        print("Very good")
    elif grade >= 75:
        print("Good")
    elif grade >= 65:
        print("Satisfactory")
    elif grade >= 60:
        print("Marginal")
    else:
        print("Unsatisfactory")