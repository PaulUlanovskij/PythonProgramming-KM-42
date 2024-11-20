import re

BIRTH_ARCIVE = "archive/"

male_dict = dict()
female_dict = dict()

for i in range(1880, 2020):
    file = open(f"{BIRTH_ARCIVE}yob{i}.txt")
    data = file.read()

    female = re.search(r"\w+(?=,F,)", data)[0]
    male = re.search(r"\w+(?=,M,)", data)[0]

    old_value = female_dict.get(female, 0)
    female_dict[female] = old_value+1

    old_value = male_dict.get(male, 0)
    male_dict[male] = old_value+1

males = list(zip(male_dict.values(), male_dict.keys()))
females = list(zip(female_dict.values(), female_dict.keys()))

males.sort(reverse=True)
females.sort(reverse=True)

for p in males:
    print(p[1], p[0])
print()
for p in females:
    print(p[1], p[0])
