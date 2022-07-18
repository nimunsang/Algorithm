N, M = map(int, input().split())

answer = 0

if N == 1 or M == 1:
    answer = 1

elif N == 2:
    answer = min(4, (M-1)//2 + 1)

else:
    if M == 2:
        answer = 2
    elif M == 3:
        answer = 3
    elif M == 4:
        answer = 4
    elif M == 5:
        answer = 4
    elif M == 6:
        answer = 4
    elif M == 7:
        answer = 5
    else:
        answer = 5 + (M-7)

print(answer)


