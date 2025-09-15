# this example will show how to display the statistical description of values

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 =int(input('Enter the third number: '))

minimum = number1

if number2 < number1:
    minimum = number2

if number3 < number1:
    minimum = number3

print('The value of minimum is:', minimum)

# getting the min and max via built in function

min(2, 7, 99)
print(min)

max(994, 9974, 87)
print(max)