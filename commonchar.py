# Python3 program to print common characters
# of two Strings in alphabetical order


# Initializing size of array
MAX_CHAR = 26


# Function to find similar characters
def printCommon(s1, s2):
    # two arrays of length 26 to store occurrence
    # of a letters alphabetically for each string
    a1 = [0 for i in range(MAX_CHAR)]
    a2 = [0 for i in range(MAX_CHAR)]

    length1 = len(s1)
    length2 = len(s2)

    for i in range(0, length1):
        a1[ord(s1[i]) - ord('a')] += 1

    for i in range(0, length2):
        a2[ord(s2[i]) - ord('a')] += 1

    # If a common index is non-zero, it means
    # that the letter corresponding to that
    # index is common to both strings
    for i in range(0, MAX_CHAR):
        if a1[i] != 0 and a2[i] != 0:

            # Find the minimum of the occurrence
            # of the character in both strings and print
            # the letter that many number of times
            for j in range(0, min(a1[i], a2[i])):
                ch = chr(ord('a') + i)
                print(ch, end='')


# Driver code
if __name__ == "__main__":
    s1 = "geeksforgeeks"
    s2 = "practiceforgeeks"
    printCommon(s1, s2)


