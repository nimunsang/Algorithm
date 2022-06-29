import heapq

N = int(input())
card_list = [int(input()) for _ in range(N)]

heapq.heapify(card_list)

answer = 0

while card_list:
    a = heapq.heappop(card_list)
    if card_list:
        b = heapq.heappop(card_list)
    else:
        break

    next = a+b
    heapq.heappush(card_list, next)
    answer += next

print(answer)

