# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self, data):
#         self.head = Node(data)
#         self.size = 0
#
#     def get_node(self, index):
#         cur = self.head
#         i = 0
#         while i < index:
#             cur = cur.next
#             i += 1
#         return cur
#
#
#     def size(self):
#         return self.size
#
#
#     def append(self, data):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(data)
#         self.size += 1
#
#
#     def insert(self, index, value):
#         new_node = Node(value)
#         self.size += 1
#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
#
#         node = self.get_node(index-1)
#         next_node = node.next
#         node.next = new_node
#         new_node.next = next_node
#
#
#     def delete(self, index):
#         self.size -= 1
#         if index == 0:
#             self.head = self.head.next
#             return
#
#         node = self.get_node(index-1)
#         node.next = node.next.next
#
#
#     def show(self):
#         string = ""
#         cur = self.head
#         while cur.next is not None:
#             string += cur.data
#             cur = cur.next
#
#         return string
#
#
#
# import sys
# input = sys.stdin.readline
#
# T = int(input())
# for _ in range(T):
#     S = input().rstrip()
#     linkedlist = LinkedList([])
#
#     cursor = 0
#     for a in S:
#         if a == '<':
#             if cursor > 0:
#                 cursor -= 1
#
#         elif a == '>':
#             if cursor < linkedlist.size:
#                 cursor += 1
#
#         elif a == '-':
#             if cursor > 0:
#                 linkedlist.delete(cursor)
#                 cursor -= 1
#
#         else:
#             linkedlist.insert(cursor, a)
#             cursor += 1
#
#     print(linkedlist.show())


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    left, right = [], []

    for a in S:
        if a == '<':
            if left:
                right.append(left.pop())

        elif a == '>':
            if right:
                left.append(right.pop())

        elif a == '-':
            if left:
                left.pop()

        else:
            left.append(a)

    print(''.join(left + right[::-1]))



