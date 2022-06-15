#Assign every lowercase value a letter from 1 to 26.
#Given a string of letters find the sum of the letters in the string.

#Step 1: Assign all the values for the letters
#Step 2: Find the length of the inputted string
#Step 3: For the length of the string check each 


def convert(x): #Converts the value of X into the subsequent number value 
    return (x-96) 

def lettersum(string): #Takes a string and finds the sum of the letters
    
    length = len(string) #Length of string
    i = 0 #Counter variable
    suma = 0 #Sum Variable
    
    while (i < length): #While loop until the end of the string
        letter = string[i] #Finds the first letter of the string
        x = ord(letter) #Changes the letter to its ascii value

        if ( (x >= 97) and (x <= 122)): #If its less than 97 and greater and 122
            suma = convert(x) + suma #Convert and add to sum
        i = i+1

    return suma #Returns the sum

#Completed

            
    
