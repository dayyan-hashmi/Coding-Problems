def filter_list(l):
    
    i = 0 #Variable Coutner
    length = len(l) - 1 #Length of original list
    l2 = [] #Duplicated list for appending
    
    while(i <= length): #Iterate until the end of the list
        
        try: #Try adding 10 since only integers can add
            l[i] = l[i] + 10
            l[i] = l[i] - 10 #Remove 10 to get back to the same value
        except: #If the try statement doesn't work, I know that it is a non integer. Just move on
            i = i + 1
        else: #Append the integer to the new list and iterate again
            l2.append(l[i])
            i = i + 1
    
    return l2 #Return the final list.
    
    'return a new list with the strings filtered out'
