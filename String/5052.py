def devide(l, idx):
    global mask
    if mask == 0:
        return

    devide_lst = [[] for _ in range(10)]
    for i in range(len(l)):
        if idx == len(l[i]):
            mask = 0
            return
        devide_lst[int(l[i][idx])].append(l[i])

    for i in range(10):
        if len(devide_lst[i]) >= 2:
            devide(devide_lst[i], idx+1)


T = int(input())
for _ in range(T):
    N = int(input())
    lst = [input() for __ in range(N)]
    mask = 1
    devide(lst, 0)
    print("YES" if mask else "NO")

