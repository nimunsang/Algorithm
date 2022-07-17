import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def find_second_max(lst):
    return sorted(lst)[2]


def make_22square_list(arr, row, col):
    return [arr[row*2][col*2], arr[row*2][col*2+1],
            arr[row*2+1][col*2], arr[row*2+1][col*2+1]]


def divide(array, size):
    if size == 1:
        return array[0][0]

    tmp = [[0]*(size//2) for _ in range(size//2)]

    for i in range(size//2):
        for j in range(size//2):
            lst = make_22square_list(array, i, j)
            tmp[i][j] = find_second_max(lst)

    return divide(tmp, size//2)

print(divide(arr, N))


