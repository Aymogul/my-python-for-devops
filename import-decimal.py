from decimal import Decimal

principal = Decimal('1000.00')

print(principal)

rate = Decimal('0.05')
print(rate)

x = Decimal('10.5')
y = Decimal('2')
print(x + y)
print(x // y)
print(x)


for year in range(1, 11):
    amount = principal * (1 + rate) ** year 
    print(f'{year:>2}{amount:>10.2f}')
    # {amoun:10.2f} means:in a field of width 10 characters
    # .2f = format as a fixed-point number with 2 decimal places