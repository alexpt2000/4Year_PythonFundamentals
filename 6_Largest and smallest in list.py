def MaxMin(list):
    minValue = min(list)
    maxValue = max(list)
    return  minValue, maxValue

list = []

num = int(input('How many numbers int the list: '))

for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)




print("Min and Max element in the list is :", MaxMin(list))

