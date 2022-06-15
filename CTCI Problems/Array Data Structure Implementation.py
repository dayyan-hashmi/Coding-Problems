#Implementing arrays in Python
#Standard Practice of Arrays
#Do linked lists in C++

x = [1,2,3,4,5,6,7]

#Implementing: Size, isEmpty, atIndex, push(item), insert(index,item)
#prepend(item), pop(), delete(index), remove(item), find(item),

#not implemented, resize(new_capacity), and capacity -> For linked lists use C++


def size(x): #Number of items in the array
    return len(x)

def isEmpty(x):
    if not x:
        return ('X is an empty list')

def atIndex(x,index):
    return (x[index])

def push(x,item):
    length = size(x) + 1
    x[length] = item
    return x

def insert(x,index,item): #Works
    length = len(x)
    i = length
    

    while (i-1 > index):
        x[i-1] = x[i-2]
        i = i-1

    x[index] = item;
    return x
    
def pop(x):
    length = len(x) - 1
    return (x[length])

def delete(x,index): #Works just doesn't delete last element. Definetely some way to do it.
    length = len(x) - 1
    j = index
    i = j + 1

    while (j != length):
        x[j] = x[i];
        j = j + 1;
        i = i + 1;

    x[-1] = ("NULL")

    return x

def remove(x,item):
    x.remove(item)
    return x

def find(x,item):
    length = len(x)-1
    int i = 0

    while (i < length):
        if (x[i] == item):
            return i
        else:
            i = i + 1




    
