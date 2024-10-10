from datetime import datetime

data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]

print(f"| {data[0][0] : ^9} | {data[0][1] : ^19} | {data[0][2] : ^9} | {data[0][3] : ^10} | {data[0][4] : ^18} | {data[0][5] : ^6} | {data[0][6] : ^4} | {data[0][7] : ^26} |")
print(f"+{'-'*11}+{'-'*21}+{'-'*11}+{'-'*12}+{'-'*20}+{'-'*8}+{'-'*6}+{'-'*28}+")
for i in range(1, len(data)):
    (code, cost, country, city, street, build, app, date) = data[i]
    print(f"| {code : <9} | {cost/1000 : >19.3f} | {country : <9} | {city : <10} | {street : <18} | {build : >6} | {app : >4} | {date.isoformat(timespec='microseconds') : >26} |")
