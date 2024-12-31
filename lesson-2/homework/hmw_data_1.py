
##1
num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print(f"The number rounded to 2 decimal places is: {rounded_num}")

##2 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

##3
kilometers = float(input("Enter distance in kilometers: "))
meters = kilometers * 1000
centimeters = kilometers * 100000

print(f"{kilometers} kilometers is equal to {meters} meters and {centimeters} centimeters.")

##4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

integer_division = num1 // num2
remainder = num1 % num2

print(f"The result of integer division is: {integer_division}")
print(f"The remainder is: {remainder}")


#5
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
#6
number = int(input("Enter a number: "))
last_digit = abs(number) % 10

print(f"The last digit of the number is: {last_digit}")

#7 
number = int(input("Enter a number: "))

if number % 2 ==0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
