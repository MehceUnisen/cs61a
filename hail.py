def f(n):
    if n == 1:
        print('done')
        return
    elif n % 2 == 0:
        print(n)
        f(n / 2)

    else:
        print(n)
        f(n * 3 + 1)

f(10)
