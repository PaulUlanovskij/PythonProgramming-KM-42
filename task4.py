salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
indexed_salary_list = []
indexation_sum_list = []

print("Salary table")
for s in salary_list:
    indexation_sum = round(s * 0.3, 2)
    indexation_sum_list.append(indexation_sum)
    indexed_salary = round(s + indexation_sum)
    indexed_salary_list.append(indexed_salary)
    print(s, indexed_salary, indexation_sum)
    

