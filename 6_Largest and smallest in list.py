list = []

num = int(input('How many numbers int the list: '))

for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)

print("Largest element in the list is :", max(list))
print("Smaller element in the list is :", min(list))
