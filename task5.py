print("Enter some elements one by one and when you are done write '__print' to output formated list")
elements = []
while True:
    element = ""
    try:
        element = input("Enter the element : ")
    except:
        break
    if element == "__print":
        break
    elements.append(element)

e_len = len(elements)
if e_len == 0:
    None
elif e_len == 1:
    print(elements)
else:
    for i in range(0, e_len-2):
        print(elements[i], end=', ')
    print(elements[-2], 'and', elements[-1])