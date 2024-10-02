print("""Unique letter sets comparer.\nTo exit the program enter "__exit" """)
while True:
    first_sentence_unique = {}
    second_sentence_unique = {}
    text = ""
    try:
        text = input("Enter first phrase : ")
    except:
        break
    if text == "__exit":
        break

    first_sentence_unique = set(a for a in text.lower() if str(a).isalpha())
    
    try:
        text = input("Enter second phrase : ")
    except:
        break
    if text == "__exit":
        break

    second_sentence_unique = set(a for a in text.lower() if str(a).isalpha())

    print("\nSet of unique letters in the first phrase :")
    print(first_sentence_unique)
    print("\nSet of unique letters in the second phrase :")
    print(second_sentence_unique)

    for c in second_sentence_unique:
        if c not in first_sentence_unique:
            break
    else:
        print("\nSecond phrase can be formed from the first one\n")
        continue
    print("\nSecond phrase can not be formed from the first one\n")
