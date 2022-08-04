import math

def ispalin(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            return False
    return True


visited = [0] * 1003002
visited[1] = 1
for i in range(2, int(math.sqrt(1003002)+1)):
    if not visited[i]:
        for j in range(2*i, 1003002, i):
            visited[j] = 1


N = int(input())
for i in range(N, 1003002):
    if not visited[i] and ispalin(i):
        print(i)
        break

