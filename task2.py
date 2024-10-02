province_index_table = {
    'A': ['Newfoundland'],
    'B': ['Nova Scotia'],
    'C': ['Prince Edward Island'],
    'E': ['New Brunswick'],
    'G': ['Quebec'],
    'H': ['Quebec'],
    'J': ['Quebec'],
    'K': ['Ontario'],
    'L': ['Ontario'],
    'M': ['Ontario'],
    'N': ['Ontario'],
    'P': ['Ontario'],
    'R': ['Manitoba'],
    'S': ['Saskatchewan'],
    'T': ['Alberta'],
    'V': ['British Columbia'],
    'X': ['Nunavut', 'Northwest Territories'],
    'Y': ['Yukon']
}

print("Canadian postal codes analyser. \nTo exit enter 'exit'")
while True:
    index = ""
    try:
        index = input("\nPlease enter the canadian postal index : ")
    except:
        break

    if index == "exit":
        break

    if len(index) != 3:
        print("Postal index must be three characters long")
        continue
    if not str(index[0]).isalpha() or not str(index[2]).isalpha():
        print("Postal index must be of format <LDL>, where L - letter, D - digit")
        continue
    if not str(index[1]).isdigit():
        print("Postal index must be of format <LDL>, where L - letter, D - digit")
        continue

    index = index.upper()

    if index[0] not in province_index_table:
        print("Invalid postal index, nonexistent province code", index[0])
        continue

    province = province_index_table[index[0]]
    is_in_city = int(index[1]) > 0

    print(f"Postal index {index} is bound to the addressee in ", end='')
    if is_in_city:
        print("city ", end='')
    else:
        print("rural ", end='')

    print("area of province ", end='')
    print(province[0], end='')

    for i in range(1, len(province)):
        print(" or", province[i], end='')

    print()
