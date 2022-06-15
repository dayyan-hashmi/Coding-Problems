def duplicate_count(text):
    
    #Initilizes counter variables
    #Initilize mapkey array (to check for duplicates) and other variables
    #Checks till last letter, if the string @ i and string @ j are equal then checks the array if it is a duplicate
    #Adds to counter and returns it.
    
    i = 0
    j = 0
    count = 0
    map = []
    string = text.lower()
    length = len(string) - 1
    
    while (i < length):
        j = i + 1
        while (j <= length):
            if (string[i] == string[j]):
                if (string[j] in map):
                    pass
                else:
                    count = count + 1
                    map.append(string[j])
            j = j + 1
        i = i + 1   
    return count
    
    
    # Your code goes here
     
