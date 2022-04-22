def smlt(*a):
    i = 1
    for val in a:
        i*=int(val)
        
    return(i)
    
def rmlt(*a):
    if len(a):
        return a[-1] * rmlt(*a[:-1])
    else:
        return 1

def bmi(heigh, mass, name):
    return{'name': name, 'bmi':float(mass)/float(heigh)/float(heigh)}