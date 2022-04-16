#lab03d
s0 = 'xxx xxx\nyy yy\nzzz zzzzz'

def subsplit (lst):
    return [sublist.split(' ') for sublist in lst.split('\n')]
    
def subwork(lst):
    tmp = []
    for line in lst:
        tmp.append([word.capitalize() for word in line])
        
    return tmp
    
if __name__ == "__main__":
    s = subsplit(s0)
    print(s)
    print(subwork(s))
