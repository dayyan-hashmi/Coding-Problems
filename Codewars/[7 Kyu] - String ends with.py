def solution(string, ending):
    
    length = len(ending) - 1
    
    if(len(ending) > len(string)):
        return False
    
    counter = - 1
    
    while (length >= 0):
        if (ending[length] == string[counter]):
            pass
        else:
            return False
        
        counter = counter - 1
        length = length - 1
    
    
    return True
