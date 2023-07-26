def f(x, y):
    if max(x,y) % min(x,y) == 0:
        return min(x,y)
    return f(min(x,y), max(x,y) % min(x,y))

print(f(40,40))