# This begins an Array Practice Problem File from Cracking_The_Coding_Interview.pdf
# Each Problem will be labeled by its number the description


# 1.1 - Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures.

def Unique(string):  # Completed
    i = 0;
    j = 0;
    k = 0;
    length = (len(string) - 1)

    while (i <= length):
        k = i + 1
        while (k <= length):
            if (string[i] == string[k]):
                return False
            k = k + 1
        i = i + 1
    return True


# /////////////////////////////////////////////////////////////////////////////

# 1.3 - URLify: Write a method to replace all spaces in a string with '%20'

mrjohn = ['M', 'R', '', 'J', 'O', 'H']


def URLify(string):  # Completed but a little wonky tbh.
    i = 0
    length = len(string) - 1

    while (i <= length):
        if (string[i] == ''):
            string[i] = '%20'
        i = i + 1

    return string


# /////////////////////////////////////////////////////////////////////////////


# 1.4 - Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome
# Not limited to dictionary words.


def Palindrome(string):  # 85% completed. Missing e, i, o functionality which is a very simple fix one line
    # Also missing space functionality which is more difficult

    # There will be three checks for the palindrome. First is the even check, second is the vowel check
    # Third is the repeating check.
    # comment

    length = len(string)

    if (length % 2 == 0):  # Even Test
        print(length)
        return False

    i = 0;
    x = 0;
    flag = False

    if (length == 3):
        count = (length - 3) / 2
        count = count + 1
        num = 0

        i = 0
        j = 0

        while (j <= length - 1):
            i = j + 1
            while (i <= length - 1):
                if (string[j] == string[i]):
                    num = num + 1;
                    return True
                i = i + 1
            j = j + 1

        print("Checking Test 3")
        print(num)
        print(count)

    ##        if (num == 1):
    ##            return True
    ##        else:
    ##            print("Fails Test 3")
    ##            return False
    ##
    while (i <= length - 1):
        if (ord(string[i]) == 97):  # Only for a currently
            x = i + 1
            while (x < length - 1):
                if (string[x] == string[i]):
                    flag = True
                    i = length + 25
                    print("Passes Test 2")
                    break
                x = x + 1
        i = i + 1

    if (flag == False):
        print("Failes Test 2")
        return False

    count = (length - 3) / 2
    count = count + 1
    num = 0

    i = 0
    j = 0

    while (j <= length - 1):
        i = j + 1
        while (i <= length - 1):
            if (string[j] == string[i]):
                num = num + 1;
                break
            i = i + 1
        j = j + 1

    print("Checking Test 3")
    print(num)
    print(count)

    if (num == count):
        return True
    else:
        print("Fails Test 3")
        return False


# /////////////////////////////////////////////////////////////////////////////

# 1.6 - String Compressions: Implement a method to perform basic string operations on repeated characters
# aabcccccaaa would become a2b1c5a3. If the compressed string is not smaller then dont return. Assume only
# upper and lower case.

letter = ("aabcccccaaa")  # Test string


def stringComp(letter):
    i = 0
    j = 0
    counter = 1
    lett2 = []
    length = len(letter) - 1

    while (i <= length):
        j = i + 1
        while (j <= length):
            if ((letter[i] == letter[j]) and (j != length)):
                counter = counter + 1
            elif (j == length and (letter[i] == letter[j])):
                counter = counter + 1
                lett2.append(letter[i])
                lett2.append(str(counter))
                i = j
                break
            else:
                lett2.append(letter[i])
                lett2.append(str(counter))
                i = j - 1
                counter = 1
                break
            j = j + 1

        if (i == length and i != j):
            lett2.append(letter[i])
            lett2.append(str(counter))

        i = i + 1

    return lett2

# Completed
