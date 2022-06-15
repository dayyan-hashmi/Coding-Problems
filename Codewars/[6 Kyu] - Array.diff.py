def remove(a, x):
    newa = []
    
    for i in a:
        if (i != x):
            newa.append(i)
    return newa

def array_diff(a, b):
    
    for x in b:
        a = remove(a,x)
    return a
    
    #your code here
