import time

lst = [i for i in range(10000000)]


def test():
    new_lst = []
    start = time.time()
    for i in range(len(lst)):
        new_lst.append(i)
    print(time.time() - start)


    new_lst = []
    start = time.time()
    for l in lst:
        new_lst.append(i)
    print(time.time() - start)


test()
