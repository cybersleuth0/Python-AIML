# string="ayush"

# for i in string:
#     print(i)

#print vowels in string

# word="ayush"
# for i in word:
#     if i in "aeiouh":
#         print(i)

#range(start,stop,step) start and step are optional
# for i in range(1,11,2):
#     print(i)

#sum of first n numbers

num=int(input("Enter a number: "))

totalSum=0
for i in range(1,num+1): 
    totalSum+=i
print("The sum of first",num,"numbers is:",totalSum)