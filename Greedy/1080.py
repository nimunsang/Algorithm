N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


if N < 3 or M < 3:
    if A == B:
        print(0)
    else:
        print(-1)
else:
    answer = 0
    for row in range(N-2):
        for col in range(M-2):
            if A[row][col] != B[row][col]:
                for i in range(3):
                    for j in range(3):
                        A[row + i][col + j] = (A[row + i][col + j] + 1) % 2

                answer += 1

    print(-1 if A != B else answer)

