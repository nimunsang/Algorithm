from collections import Counter
import sys
input = sys.stdin.readline

y, x, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

row, column = 3, 3


def Sort():
    maxlength = 0
    for i in range(len(A)):
        counter = Counter(A[i])
        if 0 in counter:
            counter.pop(0)
        A[i] = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        A[i] = [c for b in A[i] for c in b]

        if len(A[i]) > 100:
            A[i] = A[i][:100]

        maxlength = max(maxlength, len(A[i]))


    for i in range(len(A)):
        A[i] += [0] * (maxlength - len(A[i]))

    return maxlength


def R():
    global column
    column = Sort()


def C():
    global row, A
    A = list(map(list, zip(*A)))
    row = Sort()
    A = list(map(list, zip(*A)))


cnt = 0
while cnt <= 100:
    if y-1 < row and x-1 < column and A[y-1][x-1] == k:
        print(cnt)
        break
    if row >= column:
        R()
    else:
        C()
    cnt += 1

    for a in A:
        print(*a)
else:
    print(-1)

