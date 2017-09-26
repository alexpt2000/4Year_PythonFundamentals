fizzbuzz = ''

for i in range(1,100+1):
    if i%3 == 0:
        fizzbuzz += "fizz"
    if i%5 == 0:
        fizzbuzz += "buzz"
    if i%3 != 0 and i%5 != 0:
        fizzbuzz += str(i)

    fizzbuzz += '\n'

print(fizzbuzz)
