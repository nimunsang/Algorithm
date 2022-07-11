import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

S = input().rstrip()

stack = []
for num in S:
    while K and stack and int(num) > int(stack[-1]):
        stack.pop()
        K-=1
    stack.append(num)

while K:
    stack.pop()
    K -= 1

print(''.join(stack))