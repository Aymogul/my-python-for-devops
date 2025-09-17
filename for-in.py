# the basic idea behind for loop is iteration
# for variable in sequence_name


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