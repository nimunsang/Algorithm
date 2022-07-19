import sys
input = sys.stdin.readline


S = input().rstrip()
Q = int(input())

counter = [[0]*len(S) for _ in range(ord('z')-ord('a')+1)]
counter[ord(S[0])-97][0] = 1

for i in range(1, len(S)):
    for j in range(ord('z')-ord('a')+1):
        if j == ord(S[i]) - 97:
            counter[j][i] = counter[j][i-1] + 1
        else:
            counter[j][i] = counter[j][i-1]

for _ in range(Q):
    a, l, r = input().split()
    a, l, r = ord(a)-97, int(l), int(r)
    if l == 0:
        print(counter[a][r])
    else:
        print(counter[a][r] - counter[a][l-1])
