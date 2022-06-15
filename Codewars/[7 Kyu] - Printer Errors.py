from fractions import Fraction

def printer_error(s):
    
    denom = len(s)
    num = 0
    
    for i in s:
        if (ord(i) > 96 and ord(i) < 110):
            pass
        else:
            num = num + 1
    
    return (str(num) + '/' + str(denom)) 

    # your code