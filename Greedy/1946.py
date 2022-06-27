T = int(input())
for _ in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort()
    stack = [lst[0][1]]
    for i in range(1, N):
        if lst[i][1] < stack[-1]:
            stack.append(lst[i][1])

    print(len(stack))