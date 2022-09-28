K = int(input())
lst = list(input().split())

ans_min = 10**10
ans_max = -10**10


def dfs(idx, string):
    global ans_min, ans_max
    if idx == K+1:
        ans_min = min(ans_min, int(string))
        ans_max = max(ans_max, int(string))
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0:
                visited[i] = 1
                dfs(idx + 1, string + str(i))
                visited[i] = 0

            else:
                if eval(string[idx-1] + lst[idx-1] + str(i)):
                    visited[i] = 1
                    dfs(idx + 1, string + str(i))
                    visited[i] = 0


visited = [0] * 10
dfs(0, '')
print(str(ans_max).zfill(K+1))
print(str(ans_min).zfill(K+1))