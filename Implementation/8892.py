T = int(input())

def check(c):
    if c == c[::-1]:
        print(c)
        return 1

    return 0

for _ in range(T):
    K = int(input())
    lst = [input() for _ in range(K)]
    complete = 0
    for i in range(len(lst)-1):
        for j in range(i + 1, len(lst)):
            if check(lst[i] + lst[j]):
                complete = 1
                break
            if check(lst[j] + lst[i]):
                complete = 1
                break

        if complete:
            break

    else:
        print(0)