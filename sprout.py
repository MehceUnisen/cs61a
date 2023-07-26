def tree(val, branches=[]):
    return [val] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


x = tree(1, [tree(2), tree(3)])


def sprout(t, vals):
    x = list()
    if branches(t) == []:
        return tree(label(t), [tree(a) for a in vals])

    for b in branches(t):
        x += [sprout(b, vals)]
    return tree(label(t), x)


def sprout_leaves(t, vals):
    if not branches(t):
        return tree(label(t), [tree(val) for val in vals])
    else:
        new_branches = [sprout_leaves(branch, vals) for branch in branches(t)]
        return tree(label(t), new_branches)


def print_tree(t, indent=0):
    print(' '*indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)


t = sprout(x, [6, 1, 2])
print_tree(t)
