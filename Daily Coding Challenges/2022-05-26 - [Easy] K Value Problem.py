#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def listkcheck(numbers,k):
    i = 0;
    j = 0;
    length = len(numbers)

    while(i != length):
        while(j < length):
            if( numbers[i] + numbers[j] == (k)):
                return 1
            else:
                j = j+1
        i = i+1
    return 0


#Completed
#Time Complexity is Thetha(n^2) due to nested loop up until N.
#Defo a better solution. Will search up and post underneath
