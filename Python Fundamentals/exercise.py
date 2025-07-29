# Write a program to check if a given number is Positive, Negative, or Zero. (if-else)
def number_type(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative.")
    else:
        print("Zero")

number_type(2)


# Write a program to check if a given number is odd or even. (if-else)
def oddEven(num):
    if num % 2 == 0:
        print("Even.")
    else:
        print("Odd.")

oddEven(24)


# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57. (if-else)
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true
def sameLastDigit(num1, num2):
    if num1 % 10 == num2 % 10:
        return True
    else:
        return False

sameLastDigit(12,22)


# Write a program to print numbers from 1 to 10 in a single row with one tab space. (for)
def print_numbers_with_tabs():
    for i in range(1, 11):
        print(i, end='\t')
    print() # Print a final newline to move to the next line
    print("-" * 25)
    print("\n")

# Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row. (for)
def printNum(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
    print("-" * 25)
    print("\n")


# Write a program to check if a given number is prime or not. (for)

# Write a program to print prime numbers between 10 and 99. (for)

# Write a program to print the sum of all the digits of a given number. (while)
# Example:
# I/P:1234
# O/P:10

# Write a program to reverse a given number and print. (while)
# Example:1
# I/P: 1234
# O/P:4321
# Example:2
# I/P:1004
# O/P:4001

# Write a program to find if the given number is palindrome or not. (while)
def check_palindrome_number(number):
    if number < 0:
        print(f"{number} is negative and can't be palindrome.")
        return

    original_num = number
    reversed_num = 0

    if number == 0:
        print(f"{original_num} is a palindrome.")
        return

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

print("--- Check Palindrome Number ---")
check_palindrome_number(110011)
check_palindrome_number(1234)
check_palindrome_number(121)
check_palindrome_number(0)
check_palindrome_number(-121)
print("-" * 25)
print("\n")