# ============================================================================
# PYTHON FUNDAMENTALS - ASSIGNMENT 2
# ============================================================================
# Note: To solve some of the assignment Qs, we'll have to learn some additional
# logic (already mentioned as hints). The purpose of these questions is to help
# build programming logic so even if we have to take hint for mathematical part
# of the problem & we write the Python code on our own, it's alright.
# ============================================================================


# ----------------------------------------------------------------------------
# Q1: SALARY TAX CALCULATOR
# Task: Take salary as input from the user.
#       Using conditional statements, calculate the final salary based on tax:
#         • If salary < 30,000      → 5% tax
#         • If salary is 30,000–70,000 → 15% tax
#         • If salary > 70,000      → 25% tax
# Hint: final_salary = salary - (salary * tax_rate / 100)
# ----------------------------------------------------------------------------

# salary = float(input("Enter your salary: "))
# Write your logic here

# salary = float(input("Enter your salary: "))
# if salary < 30000:
#     tax_rate = 5
# elif 30000 <= salary <= 70000:
#     tax_rate = 15
# else:
#     tax_rate = 25
# final_salary = salary - (salary * tax_rate / 100)
# print(f"Your final salary after tax is: {final_salary} and tax rate applied is: {tax_rate}%")



# ----------------------------------------------------------------------------
# Q2: PRINT EVEN NUMBERS BETWEEN TWO INTEGERS
# Task: Write a function that takes two integers (start, end)
#       and prints all even numbers between them (inclusive).
# Hint: Use a loop and check if number % 2 == 0
# ----------------------------------------------------------------------------

# def print_evens(start, end):
#     Write your logic here

# number1 = int(input("Enter the first integer: "))
# number2 = int(input("Enter the second integer: "))
# print(f"Even numbers between {number1} and {number2} are:")
# for num in range(number1, number2 + 1):
#     if(num % 2 == 0):
#         print(num, end=' ')


# ----------------------------------------------------------------------------
# Q3: PRINT DIGITS OF A NUMBER
# Task: Write a function that prints the digits of a number n.
#       Example: n = 312 → print 3, 1, and 2
#
# Hints:
#   • The rightmost digit of a number N is: N % 10
#   • To remove the rightmost digit: N = N // 10 (integer division)
#   • Use a while loop until N > 0
# Note: This will print digits in reverse order (right to left)
# ----------------------------------------------------------------------------

# def print_digits(n):
#     Write your logic here

# number = int(input("Enter a number: "))
# print(f"The digits of the number {number} are:")
# while number > 0:
#     digit = number % 10 # Extract the rightmost digit
#     print(digit, end=' ') # Print the digit followed by a space
#     number = number // 10 # Remove the rightmost digit by performing integer division


# ----------------------------------------------------------------------------
# Q4: COUNT NUMBER OF DIGITS
# Task: Write a function to return the count of digits in a number n.
# Hint: Use a while loop with N = N // 10 and keep a counter
# ----------------------------------------------------------------------------

# def count_digits(n):
#     Write your logic here

# def count_digits(n):
#     count = 0
#     while n > 0:
#         n = n // 10 # Remove the rightmost digit
#         count += 1 # Increment the count for each digit removed
#     return count

# print(count_digits(12345)) # Output: 5

# ----------------------------------------------------------------------------
# Q5: SUM OF DIGITS
# Task: Write a function to return the sum of digits of a number n.
# Hint: Use N % 10 to extract each digit and add it to a running total
# ----------------------------------------------------------------------------

# def sum_of_digits(n):
#     Write your logic here

# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10 # Extract the rightmost digit
#         total += digit # Add the digit to the total sum
#         n = n // 10 # Remove the rightmost digit by performing integer division
#     return total
# print(sum_of_digits(12345)) # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)


# ----------------------------------------------------------------------------
# Q6: DIVISIBLE BY BOTH 3 AND 5
# Task: Write a program to print all numbers from 1 to 100
#       that are divisible by both 3 and 5.
# Hint: A number divisible by both 3 and 5 means number % 3 == 0 and number % 5 == 0
#       (or simply: number % 15 == 0)
# ----------------------------------------------------------------------------

# Write your logic here
# for num in range(1, 101):
#     if num % 15 == 0: # Check if the number is divisible by both 3 and 5
#         print(num) # Print the number followed by a space


# ----------------------------------------------------------------------------
# Q7: POSITIVE OR NEGATIVE UNTIL QUIT
# Task: Design a program to continuously input a number from the user
#       and print if it is positive or negative,
#       until the user enters "Quit".
# Hint: Use a while True loop with a break condition when input is "Quit"
# ----------------------------------------------------------------------------

# Write your logic here
# input_str = input("Enter a number (or 'Quit' to exit): ")
# while True:
#     if input_str.lower() == "quit": # Check if the user wants to quit
#         print("Exiting the program. Goodbye!")
#         break # Exit the loop
#     try:
#         number = float(input_str) # Try to convert the input to a number
#         if number > 0:
#             print(f"{number} is positive.")
#         elif number < 0:
#             print(f"{number} is negative.")
#         else:
#             print("The number is zero.")
#     except ValueError: # Handle the case where input is not a valid number
#         print("Invalid input. Please enter a valid number or 'Quit' to exit.")
#     input_str = input("Enter a number (or 'Quit' to exit): ") # Ask for the next input


# ----------------------------------------------------------------------------
# Q8: SIMPLE CALCULATOR
# Task: Create a function calculator(a, b, operation) that performs
#       arithmetic operations based on the operation parameter.
#       operation can have values: '+', '-', '*', '/'
#
# Hint: Use if/elif to check operation and perform the corresponding math
# ----------------------------------------------------------------------------

# def calculator(a, b, operation):
#     Write your logic here
# def calculator(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero is not allowed."
#     else:
#         return "Error: Invalid operation. Please use '+', '-', '*', or '/'."

# print(calculator(10, 5, '+')) # Output: 15
# print(calculator(10, 5, '-')) # Output: 5
# print(calculator(10, 5, '*')) # Output: 50
# print(calculator(10, 5, '/')) # Output: 2.0
# print(calculator(10, 0, '/')) # Output: Error: Division by zero is not allowed.
# print(calculator(10, 5, '^')) # Output: Error: Invalid operation. Please use '+', '-', '*', or '/'.

# ----------------------------------------------------------------------------
# Q9: CHECK IF A NUMBER IS PRIME
# Task: Write a function is_prime(n) that returns True if n is a prime number,
#       and False otherwise, using a loop.
#
# Hints:
#   1. We only check prime for 2 or numbers greater than 2.
#      2 is the smallest prime number.
#   2. A non-prime number n will always get divided by at least one number
#      in range [2, n-1].
#      Example: For n=9, we check range(2, 9) → divisible by 3 → not prime
#               For n=7, we check range(2, 7) → not divisible by any → prime
# ----------------------------------------------------------------------------

# def is_prime(n):
#     Write your logic here
# for num in range(1, 101):
#     if num > 1: # Check only for numbers greater than 1
#         is_prime = True # Assume the number is prime until proven otherwise
#         for i in range(2, num): # Check divisibility from 2 to num-1
#             if num % i == 0: # If num is divisible by any i, it's not prime
#                 is_prime = False
#                 break # No need to check further, exit the loop
#         if is_prime:
#             print(f"{num} is a prime number.")
#         else:
#             print(f"{num} is not a prime number.")


# ----------------------------------------------------------------------------
# Q10: NUMBER GUESSING GAME
# Task: Create a "Number Guessing Game".
#       Given a secret number (already decided by you), write a program that
#       asks the user to guess it and prints:
#         • "Too high"    — if the guess is above the secret number
#         • "Too low"     — if the guess is below the secret number
#         • "Correct!"    — if the guess matches the secret number
#
# Hint: Use a while loop to keep asking until the user guesses correctly
# ----------------------------------------------------------------------------

secret_number = 42
# Write your logic here

while True:
    guess = input("Guess the secret number (or type 'Quit' to exit): ")
    if guess.lower() == "quit":
        print("Exiting the game. Goodbye!")
        break
    try:
        guess = int(guess) # Convert the guess to an integer
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You've guessed the secret number!")
            break # Exit the loop when the guess is correct
    except ValueError: # Handle the case where input is not a valid integer
        print("Invalid input. Please enter a valid number or 'Quit' to exit.")
