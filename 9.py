# Flow Statements 
# 1. break 
# 2. continue 

# loops 
# 1. For else 
# 2. While else 

# # Break Statement 
# for i in range(5):
#     print(i)
#     if i > 3:
#         break

# # Continue Statement 
# for i in range(5):
#     if i > 4: 
#         continue
#     print(i)

# # for else 
# for i in range(5):
#     print(i)
#     if i > 3:
#         break
# else: 
#     print("here")

i = 0
# While else 
while i <= 10:
    print(i)
    i+= 1
    if i > 2: 
        break
else : 
    print("Complete")