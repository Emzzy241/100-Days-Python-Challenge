def test(*args):
    # print(type(args))
    print(args)

# args is a tuple, it will print the parenthesis
# test(1, 2, 3, 5)

def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
# Printed out: 4 (7, 3, 0) {'x': 10, 'y': 64}
# 4 is passed by position. 7, 3, 0 are collected into a tuple x and y are in a keyword dictionary