
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

enterFactorial = int(input("input a number please "))

print("this is your number",factorial(enterFactorial))
