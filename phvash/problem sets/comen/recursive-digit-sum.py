def main(n, k):
    p = str(n)
    for i in range(1, k):
        p += str(n)
    return super_digit(p)

def super_digit(p):
    if len(p) == 1:
        return p
    else:
        sum = 0
        for digit in p:
            sum += int(digit)
        return super_digit(str(sum))

if __name__ == '__main__':
    n, k = input().strip(" ").split(" ")
    print(main(int(n), int(k)))