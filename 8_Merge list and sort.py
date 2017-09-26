def merge (l1,l2):
    if len(l1) == 0 and len(l2) == 0:
        return []
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    if l2[0] <= l1[0]:
        return [l2[0]] + merge(l1, l2[1:])


l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]

print(merge(l1+l2))
