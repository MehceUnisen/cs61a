def tree(val, branches=[]):
    return [val] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def sprout(t, vals):
    l = []
    if branches(t) == []:
        return tree(label(t), [tree(x) for x in vals])
    for b in branches(t):
        l += [sprout(b, vals)]
    return tree(label(t), l)


def print_tree(t, indent=0):
    print(' '*indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)


def copyTree(t):
    l = []
    if branches(t) == []:
        return tree(label(t))
    for b in branches(t):
        l += [copyTree(b)]
    return tree(label(t), l)


def twoTree(t, f):
    l = []
    if branches(t) == []:
        return tree(f(label(t)))
    for b in branches(t):
        l += [twoTree(b, f)]
    return tree(f(label(t)), l)


def sprout_x(t, vals):
    l = []
    if branches(t) == []:
        return tree(label(t), [tree(x) for x in vals])
    for b in branches(t):
        l += [sprout_x(b, vals)]
    return tree(label(t), l)


x = tree(1, [tree(2), tree(3)])
t = sprout_x(x, [6, 1, 2])
print_tree(t)
z = twoTree(t, lambda x: x * 2)
print_tree(z)
