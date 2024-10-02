def readString(prompt):
    while True:
        value = 0
        try: 
            value = input(prompt)
        except:
            return "exit"
        if value == "exit":
            return "exit"
        if not value.isalpha():
            print("Enter the alphabetical string")
        return value

def readInt(prompt):
    while True:
        value = 0
        try: 
            value = input(prompt)
        except:
            return "exit"
        if value == "exit":
            return "exit"
        if not value.isdigit():
            print("Enter the number consisting of digits [0-9]")
        return int(value)

print("Ukrpost receiver address formatter\nWrite 'exit' to exit the program")
while True:
    name = readString("Please enter receiver`s name : ")
    if name == "exit":
        break
    family_name = readString("Please enter receiver`s family name : ")
    if family_name == "exit":
        break
    phone_number = readInt("Please enter receiver`s phone number : ")
    if phone_number == "exit":
        break
    street_name = readString("Please enter receiver`s street`s name : ")
    if street_name == "exit":
        break
    building_number = readInt("Please enter receiver`s building`s number : ")
    if building_number == "exit":
        break
    apartament_number = readInt("Please enter receiver`s apartment`s number : ")
    if apartament_number == "exit":
        break
    city_name = readString("Please enter the name of receiver`s city : ")
    if city_name == "exit":
        break
    postal_index = readInt("Please enter receiver`s postal index : ")
    if postal_index == "exit":
        break
    country_name = readString("Please enter receiver`s country`s name : ")
    if country_name == "exit":
        break

    print(name, family_name)
    print(phone_number)
    print("Str.", street_name, building_number, end='')
    print(", ap.", apartament_number, end='')
    print(",", city_name)
    print(postal_index)
    print(country_name)