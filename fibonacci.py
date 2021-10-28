def fib(num):
    a, b = 1, 1
    for c in range(num - 1):
        a, b = b, a + b
        # print('this is A', a)
        # print('this is b', b)
        # print('this is num', num)
    return a

print(fib(3))

