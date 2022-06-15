#Given an array of integers return a new array such that the index i has the
#product of every other number except for i

#Sample [1,2,3,4,5] returns [120,60,40,30,24]

a = [1,2,3,4,5]

def productArray(a):
    i = 0
    j = 0
    k = 0
    length = len(a) - 1
    na = [0] * (length+1)

    while (i <= length):
        j = i - 1
        k = i + 1
        product = 1

        while (j >= 0):
            product = product*a[j]
            j = j - 1

        while (k <= length):
            product = product*a[k]
            k = k + 1
            
        print(product)
        na[i] = product
        i = i + 1

    return na


#Time Complexity is dogshit lol. O(n^2)
#Completed in 30 minutes alhumdullilah
