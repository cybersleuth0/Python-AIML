# i=5 #iterator
# while i>=1:
#     print(i)
#     i-=1

#Multiplication table of n

# n=int(input("Enter a number: "))

# i=1

# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# Break & Continue

# i=0
# while i<10:
#     if(i%2==0):      # checks if i is even (0 % 2 == 0 → True)
#         break        # exits the loop IMMEDIATELY
#     print(i)
#     i+=1
# print("Loop ended")


# Odd numbers 
i=0
while i<10:
    i+=1
    if(i%2==0):      # checks if i is even (0 % 2 == 0 → True)
        continue      # skips the rest of the loop and goes to the next iteration
    print(i)