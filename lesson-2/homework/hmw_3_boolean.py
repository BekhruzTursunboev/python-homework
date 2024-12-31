# Program 1
username = input("Enter username: ")
password = input("Enter password: ")
if username and password:
    print("Both username and password are valid.")
else:
    print("Username or password cannot be empty.")

# Program 2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# Program 3
number = int(input("Enter a number: "))
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

# Program 4
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a != b and b != c and a != c:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

# Program 5
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) == len(string2):
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")

# Program 6
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

# Program 7
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 + num2 > 50:
    print("The sum of the numbers is greater than 50.")
else:
    print("The sum of the numbers is not greater than 50.")

