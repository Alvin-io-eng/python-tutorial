def months_of_the_year(year : int):
    is_a_LeapYear = is_leap(year)
    months = [
       {"January":31},
    #    {"Febuary":if is_a_LeapYear: 29 else: 28}, # learn to write if statement in one line
       {"March":31},
       {"April":30},
       {"May":31},
       {"June":30},
       {"July":31},
       {"August":31},
       {"September":30},
       {"October":31},
       {"November":30},
       {"December":31}
    ]
    return months

def is_leap(year : int):
   if year % 4 == 0:
      return True
   else:
      return False

print(is_leap(2024))