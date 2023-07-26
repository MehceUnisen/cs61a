def f(x):
    z = 0
    if x <= 0:
        return 0

    return x + f(x - 2)

print(f(10))