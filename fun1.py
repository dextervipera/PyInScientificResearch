def mlt(a1, a2, print_msg=False):
    f = lambda x1,x2: x1*x2
    if print_msg:
        print(f' wynik to {f(a1,a2)}')
    return f(a1,a2)

mlt(4,5,True)