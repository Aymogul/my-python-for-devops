"""Compare integers using if statement and comparison operators"""

print('Echo two integers and i will tell you', 'the relationships they satisfy.')

#read the first integer
number1 = int(input('Enter the first integer: '))

# read the second integer
number2 = int(input('Enter the second integer: '))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)


