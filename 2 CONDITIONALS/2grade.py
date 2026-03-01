score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score >= 50 and score <= 59:
    print("Grade E")
else:
    print("Grade F")

# some flipping around

if 90 >= score and score <= 100:
    print("Grade A")
elif 80 >= score and score <= 89:
    print("Grade B")
elif 70 >= score and score <= 79:
    print("Grade C")
elif 60 >= score and score <= 69:
    print("Grade D")
elif 50 >= score and score <= 59:
    print("Grade E")
else:
    print("Grade F")

# now combine these ranges instead of asking 2 boolean expressions

if 90 >= score <= 100:
    print("Grade A")
elif 80 >= score <= 89:
    print("Grade B")
elif 70 >= score <= 79:
    print("Grade C")
elif 60 >= score <= 69:
    print("Grade D")
elif 50 >= score <= 59:
    print("Grade E")
else:
    print("Grade F")

# OR

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 50:
    print("Grade E")
else:
    print("Grade F")