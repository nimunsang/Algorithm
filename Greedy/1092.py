import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxs = list(map(int, input().split()))

cranes.sort()
boxs.sort()

answer = 0
while boxs:
    poped = 0
    for i in range(len(cranes)-1, -1, -1):
        if not boxs:
            break

        for j in range(len(boxs)-1, -1, -1):
            if cranes[i] >= boxs[j]:
                poped = 1
                boxs.pop(j)
                break

        else:
            break

    if not poped:
        answer = -1
        break

    answer += 1

print(answer)