grade = 85

if grade >= 60: 
    print('Passed')
else:
    print('Failed')

grade = 57

if grade >= 60: 
    print('Passed')
else:
    print('Failed')

grade = 99

if grade >= 60: 
    print('Passed')
else:
    print('Failed')

# Conditional Expressions

grade = 87

if grade >= 60:
    result = 'Passed'
else:
    result = 'Failed'
    
result

result = ('Passed' if grade >= 60 else 'Failed')

result

'Passed' if grade >= 60 else 'Failed'

# Multiple Statements in a Suite

grade = 49

if grade >= 60:
    print('Passed')
else:
    print('Failed')
    print('You must take this course again')

grade = 100

if grade >= 60:
    print('Passed')
else:
    print('Failed')
print('You must take this course again')

# if…elif…else Statement
grade = 77

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
