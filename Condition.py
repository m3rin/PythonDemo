# Greater OR lesser number
"""x = int(input("Enter any value: "))
if x == 10:
    print("Hello, value is 10")
elif x > 10:
    print("The number is greater than 10")
elif x < 10:
    print("The number is lesser than 10")
else:
    print("Value not found")"""


#Exercise 1) Wish According to the time
"""
import time
hour = int(time.strftime('%H'))
print("Current Time:", hour)

if hour < 12:
    print("Good Morning!")
elif hour > 12 and hour < 17:
    print("Good Afternoon!")
elif hour > 17 and hour < 19:
    print("Good Evening!")
else:
    print("Good Night!")
"""

#Match Case
"""x = int(input("Enter a number:"))
match x:
    case 1 if x == 0:
        print("Value given is zero")
    case 2 if x > 10:
        print("Value is greater than 10")
    case 3 if x < 10:
        print("Value is Lesser than 10")
    case _:
        print("Enter valid Number")
"""
"""
a = int(input("Enter first Num:"))
b = int(input("Enter second Num:"))
c = int(input("Enter third Num:"))
if a > b:
    if a > c:
        print("a is greater")
    
elif b > a:
    if b > c:
        print("b is greater") 
    else:
        print("c is greater")
"""