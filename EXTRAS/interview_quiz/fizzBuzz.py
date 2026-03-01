# FIZZ BUZZ program
# loop from 1-100
# if a no is diisible by 3 print - FIZZ
# by 5 print - BUZZ
# if is divisible by 3 & 5 then FIZZ BUZZ
# else print the No.
# now what if I want to add a new condition
# if divisble by 7 BAZZ
# how do you deal with that

# will print both FIZZ & BUZZ but for the numbers divisible by 3 & 5 but will be in the same line
for number in range(1,101):
    # print(number)
    if (number%3) == 0 and (number%5) == 0:
        print(f"{number} FIZZ BUZZ")
    elif (number%5) == 0:
        print(f"{number} BUZZ")
    elif (number%3) == 0:
        print(f"{number} FIZZ")
    else:
        print(number)

# will print both FIZZ & BUZZ but for the numbers divisible by 3 & 5 but won't be in the same line
for number in range(1,101):
    
    if (number%3) == 0:
        print(f"{number} FIZZ")
    if (number%5) == 0:
        print(f"{number} BUZZ")
    else:
        print(number)

"""

Always Be Chatting ABC rule(not always be coding) but not some duumb shit though
practice writing code out loud

TIP:/ INTERVIEWERS WANT YOU TO SUCCEED

feel free to ask questions don't get confused and freeze up

TIP:/ EXPRESS YOUR PASSION FOR CODE
TIP:/ DON'T BE TOO CLEVER - avoid language specific magic

write better code and be a better  programmer by NEVER USING ELSE STATEMENT (ELSE IF , ELIF) > ***ELSE keyword is an anti pattern

TIP:/ NEVER BELIEVE THE INTERNET
TIP:/ ALWAYS BELIEVE EVERYTHING YOU READ ON THE INTERNET *correction
----------------------------------------------------------------------------------------------------------------------
if divisble by 7 BAZZ
When you have a lot of conditions to check one thing youl'd wanna do is try to extract the data out of that statement 
we can easily do that by defining the variable we want to print
then can setup SWITCH statement (in python is MATCH . CASE) but if will do just fine if not better
instead of printing the msg in the if statement we can mutate the variable (msg += "BAZZ") - allos us to eliminate the fizz buzz check and can also scale better if we decide to add additional words to it

TIP:/ DO NOT CHEAT

Now how would you describe the performance of you algorithm ? ***strong <TIP:/ DONT SAY BLAZINGLY FAST>
You see when you run it there is no lagtime 
But when they ask the above question they usually mean/refer to the BIG-O TIME COMPLEXITY CHART

TIP:/ STUDY BIG-O
if the fizz buzz were to go on forever I'd say we have LINEAR TIME COMPLEXITY / o(n). However the gameis played for 100 steps(constant) which simplifies to o(1) OR constant time

"""

# when adding new conditions and if a number is divisible by every other number in the statement(better scaling)

for i in range(1,101):
    msg = ""
    if (i%3) == 0:
        msg += "FIZZ"
    if (i%5) == 0:
        msg += "BUZZ"
    # if (i%3) == 0 and (i%5) == 0:
    #     msg += "FIZZ BUZZ"
    if (i%7) == 0:
        msg += "BAZZ"
    
    print(msg, i ,sep=" ")

# for i in range(1,101):
#     fizz = i%3
#     buzz = i%5
#     if fizz:
#         print(f"{i} FIZZ")
#     elif buzz:
#         print(f"{i} BUZZ")
#     else:
#         print(i)