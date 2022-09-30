import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
alphabet = 'ABCDEF'
dic = dict(zip(alphabet, lst))
three = ['ABC', 'ABD', 'ACE', 'ADE', 'FBC', 'FCE', 'FDE', 'FBD']
two = ['AC', 'AB', 'AE', 'AD', 'FB', 'FC', 'FD', 'FE', 'EC', 'ED', 'DB', 'BC']

onemin = min(lst)
twomin = min([sum([dic[item[i]] for i in range(2)]) for item in two])
threemin = min([sum([dic[item[i]] for i in range(3)]) for item in three])

oneside = (N-1) * (N-2) * 4 + (N-2) * (N-2)
twoside = 8*(N-1) - 4
threeside = 4

if N == 1:
    lst.sort()
    print(sum(lst[:5]))

else:
    print(oneside * onemin + twoside * twomin + threeside*threemin)