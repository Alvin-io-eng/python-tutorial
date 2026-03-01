numbers = [1,2,3,4,5,6,7,8,9,10]

prime_numbers = []
 
type_list = []

for p in numbers:
    b = 1
    while b <= p:
        c = p/b
        d = type(c)
        type_list.append(d)
        b += 1
    counts = type_list.count("<class 'type'>")

    if counts == 2:
        prime_numbers.append(p)
        print(p)
    else:
        continue


print(type(type_list[12]))

        
        
