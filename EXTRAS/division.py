# a = 20
# b = 9
# ans = 0

# rem = a
# while rem > 0:
#     rem = rem - b
#     ans += 1
#     print(rem)
#     print(ans)
#     if rem < b:
#         break

    
# print(f"{a} / {b} is {ans} rem {rem}")

# if a >= b:
#     rem = a
#     while rem >= 1:
#         rem = rem - b
#         ans += 1    
#         # print(rem)
#         # print(ans)    
#         if rem < b:
#             break
#     print(f"{a} / {b} is {ans} rem {rem}")
# else:
#     rem = b
#     while rem >= 1:
#         rem = rem - a 
#         ans += 1
#         # print(rem)
#         # print(ans)   
#         if rem < a:
#             break
#     if rem == 0:
#         print(f"{a} / {b} is {1}/{ans}")
#     else:
#         print(f"{a} / {b} is {rem}/{ans}")
    
# GEMINI

def divide_without_operator(dividend, divisor):
    if divisor == 0:
        return "Error: Cannot divide by Zero"
    
    # Handle negative numbers
    negative = (dividend<0)^(divisor<0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    return -quotient if negative else quotient

print(f"Division (20//3): {divide_without_operator(20,3)}")

