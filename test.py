import decimal
import sys

print(round(decimal.Decimal('2.355'), 2))
print(round(2.355, 2))
print(round(2.355 + 0.000000001, 2))
print(round(4.71 / 2, 2))
print(round(decimal.Decimal('4.71') / 2, 2))
print(round(4.71 / 2 + 0.000000001, 2))


print(2.3 / 232)

lst = [5.4, 5.4, 5.4, 5.4,
5.4,
5.5,
5.5,
5.5,
5.5,
5.5,
5.6,
5.6,
5.6,
5.6,
5.7,
5.7,
5.7,
5.7, 5.7, 5.7]

print(sum(lst))
print(len(lst))
print(sum(lst) / len(lst))

lst = [5.4,
       5.4,
5.4,
5.5,
5.5,
5.5,
5.5,
5.5,
5.6,
5.6,
5.6,
5.6,
5.7,
5.7,
5.7,
5.7]

print(sum(lst) / len(lst))
