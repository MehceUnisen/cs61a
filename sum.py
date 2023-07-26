def f(x, g):
    if x == 0:
        return 0
    else:
        return g(x) + f(x - 1, g)
print(f(9, lambda x: x + 1))