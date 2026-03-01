days = {
    1:"Kaname",
    2:"Ryuu",
    3:"Tsukasa",
    4:"Masami",
    5:"Hayate",
    6:"Hajime",
    7:"Tsubasa",
    8:"Chihiro",
    9:"Setsuna",
    10:"Natsuki",
    11:"Akiho",
    12:"Yuuki",
    13:"Midori",
    14:"Naomi",
    15:"Tomo",
    16:"Hinata",
    17:"Kagami",
    18:"Riku",
    19:"Chiaki",
    20:"Makoto",
    21:"Hikaru",
    22:"Jun",
    23:"Mitsuki",
    24:"Haruka",
    25:"Kaoru",
    26:"Satsuki",
    27:"Kazumi",
    28:"Hikari",
    29:"Katsumi",
    30:"Mitsune",
    31:"Harumi"
}

months = {
    "January":["Sato",31],
    "Febuary":["Suzuki",29],
    "March":["Takahashi",31],
    "April":["Tanaka",30],
    "May":["Watanabe",31],
    "June":["Kamisato",30],
    "July":["Yamato",31],
    "August":["Nakamura",31],
    "September":["Kobayashi",30],
    "October":["Ishikawa",31],
    "November":["Saito",30],
    "December":["Yamashita",31]
}

names = []

"""
concatinate days names with month according to the number of days each month has

loop through the months 
   fetch for number of days in a month and the lastname
      loop the number of number of days and in each iteration we concatinate the names and append them to the names list


"""

def count(gimmic):
    p = 0
    for n in gimmic:
        p +=1
    print(p)

for month in months:
    # print(months[month])
    data = months[month]
    # print(data[0])
    lastname = data[0]
    no_days = data[1]
    for day in range(1,no_days+1):
        firstname = days[day]
        fullname = f"{firstname} {lastname}"
        names.append(fullname)
        
combination = count(names)

# for name in names:
#     print(names)
        
"""# print(combination)
call = []

for month in months:
    data = months[month]
    no_days = data[1]
    # print(type(no_days))
    for day in range(no_days):
        call.append(type(day))
        # name = days[day]
        # names.append(names)
        # print(day)
        break"""


"""# print(names)

for i in range(1,3+1):
    print(i)"""