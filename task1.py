import string
GADSBY_FILE = "gadsby.txt"

file = open(GADSBY_FILE)
letters_use = [0 for i in range(26)]
total_letters = 0
while True:
    try:
        letter = file.read(1).lower()
        if letter not in string.ascii_lowercase:
            continue
        letters_use[ord(letter)-97] += 1
        total_letters += 1
    except Exception:
        break
letters_use = list(zip(letters_use, string.ascii_lowercase))
letters_use.sort(reverse=True)
for i in range(5):
    print(letters_use[i][1], round(letters_use[i][0]/total_letters * 100, 3))
print()
for i in range(5):
    print(letters_use[21+i][1], round(letters_use[21+i][0]/total_letters * 100, 3))
