# Conditional Statements 

# if else, else if , 
# Basic Form 
# Complete Form 
# Ladder Form 
# Nested Form 
# Short Hand Notation (Equivalent to Ternary Operator )

a = 20 
# Basic Form 
if a >= 10 : 
    print("Inside If Condition")

# Complete Form 
if a < 20: 
    print("Inside if")
else :
    print("in else")

# Ladder Form 
# if true, else if true, else if, ...  else

a = 35 
if a <= 10:
    print("11")
elif a>= 20 and a<= 30:
    print("22")
elif a > 30 and a < 40:
    print("33")
else :
    print("none")


a = 10
# Nested Form 
if a>= 20 and a <= 40: 
    if a%2 == 0 : 
        print("Even")
    else :
        print("Odd")
else: 
    print("nhi baith raha")


# Short hand Notation 
print(a) if a >= 25 else print("No")