def __adder__(num):
    number = num.__str__()
    length = number.__len__()
    addition = 0
    for i in range(0, length):
        addition += int(number[i])
    return addition


def __super_number__(num):
    if num.__str__().__len__() == 1:
        return num
    else:
        return __super_number__(__adder__(num))


numb, k = raw_input().split()
numb = numb.__str__()
k = int(k)
new_number = numb * k

print __super_number__(new_number)

# this recursive method has a runtime error for big values of numb * k
