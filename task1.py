salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
print("Salary table:")
list(map(lambda i: print(f"{i[0]} {i[1]} {i[2]}"), list(zip(list(map(lambda x: round(x,2), salary_list)), list(map(lambda x: round(x*1.3, 2), salary_list)), list(map(lambda x: round(x*0.3,2), salary_list))))))
