#lab03
def mlt(*num, show_msg=False):
    tmp = 1
    for n in num:
        tmp = tmp * n

    if show_msg:
        print(f' wynik to {tmp}')

    return tmp

mlt(4,3,show_msg=True)
mlt(4,3,2,show_msg=True)    
mlt(4,3,2,6,8,show_msg=True)