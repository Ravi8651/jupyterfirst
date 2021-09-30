def foo(*args):
    return sum(args) / len(args)
print(foo(20, 20, 30))