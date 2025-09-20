# the basic idea behind for loop is iteration
# for variable in sequence_name, print variable


for character in 'Programming':
    print(character, end='  ')


names = ['ayo', 'deji', 'ay', 'ade']
for name in names:
    print(name)

for char in "hello":
    print(char)


for i in range(7):
    print(i)


for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(5):
    if num == 2:
        continue
    print(num)

# Function print’s sep Keyword Argument 
print(10, 20, 30, sep=', ')

# 3.8.1 Iterables, Lists and Iterators
total = 0

for number in [2, -3, 0, 17, 9]:
    total = total + number
    
total

# 3.8.2 Built-In range Function and Generators
for counter in range(10):
    print(counter, end=' ')


for number in range(5, 10):
    print(number, end=' ')

for number in range(0, 10, 2):
    print(number, end=' ')

for number in range(10, 0, -2):
    print(number, end=' ')