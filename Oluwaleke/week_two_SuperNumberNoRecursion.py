def __super_num__(num, q):
    number = num.__str__()
    length = number.__len__()
    addition = 0
    float('-inf')
    for i in range(0, length):
        addition += int(number[i])
    total = addition * q
    return total % 9

numb, k = raw_input().split()
numb = numb.__str__()
k = int(k)
result = __super_num__(numb, k)
if result == 0:
    print 9
else:
    print result
