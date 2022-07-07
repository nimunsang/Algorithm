N = int(input())
lst = [list(input()) for _ in range(N)]

answer = 0
def check():
    global answer
    for i in range(N):
        tmp = 1
        for j in range(1, N):
            if lst[i][j] == lst[i][j-1]:
                tmp += 1
            else:
                answer = max(answer, tmp)
                tmp = 1
        answer = max(answer, tmp)


    for i in range(N):
        tmp = 1
        for j in range(1, N):
            if lst[j][i] == lst[j-1][i]:
                tmp += 1
            else:
                answer = max(answer, tmp)
                tmp = 1
        answer = max(answer, tmp)



for i in range(N):
    for j in range(N):
        if j+1 < N:
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            check()
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        if i+1 < N:
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            check()
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]

print(answer)