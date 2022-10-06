import sys
input = sys.stdin.readline

answerlist = []
vis = set()
answer = 3
answerlist.append(3)
for i in range(1, 1001):
    tmp = 0
    for j in range(1, i):
        if i / j not in vis:
            vis.add(i / j)
            tmp += 1

    answer += tmp * 2
    answerlist.append(answer)


C = int(input())
for _ in range(C):
    N = int(input())
    print(answerlist[N])


