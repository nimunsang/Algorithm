n = int(input())
for _ in range(n):
    s = input().upper()
    print("Yes" if s == s[::-1] else "No")
