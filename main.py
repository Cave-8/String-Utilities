import numpy.matrix

# Matrix cell used for dynamic programming approach, contains value for alignment and "pointer" for backtracking
class matrixCell:
    value = 0
    backtrack = null

# Given two strings it returns global sequence alignment result
def globalSequenceAlignment(s1, s2):
    print("Test")
    string1 = str(s1)
    string2 = str(s2)


# Given two strings it returns local sequence alignment result
def localSequenceAlignment(s1, s2):
    print("Test")


# Given two strings it returns the longest common subsequence shared by them
def longestCommonSubsequence(s1, s2):
    print("Test")


# Given two strings it returns the longest common substring shared by them
def longestCommonSubstring(s1, s2):
    print("Test")

# End routine
def endRoutine():
    print("If you want to select a different operation digit 1, otherwise digit 2")
    choice = input("> ")
    while 1:
        if int(choice) == 2:
            exit(0)
        elif int(choice) == 1:
            return
        else:
            print("Please, digit 1 or 2")
            choice = input("> ")


# Main body
while 1:
    print("Please select operation:")
    print("1 - Global sequence alignment")
    print("2 - Local sequence alignment")
    print("3 - Longest common subsequence")
    print("4 - Longest common substring")
    op = int(input("> "))

    if int(op) == 1:
        print("Insert first string")
        s1 = input("> ")
        print("Insert second string")
        s2 = input("> ")

        try:
            s1 = str(s1)
            s2 = str(s2)
        except ValueError:
            print("Please, insert valid string")
            continue
        globalSequenceAlignment(s1, s2)
        endRoutine()

    elif int(op) == 2:
        print("Insert first string")
        s1 = input("> ")
        print("Insert second string")
        s2 = input("> ")

        try:
            s1 = str(s1)
            s2 = str(s2)
        except ValueError:
            print("Please, insert valid string")
            continue
        localSequenceAlignment(s1, s2)
        endRoutine()

    elif int(op) == 3:
        print("Insert first string")
        s1 = input("> ")
        print("Insert second string")
        s2 = input("> ")

        try:
            s1 = str(s1)
            s2 = str(s2)
        except ValueError:
            print("Please, insert valid string")
            continue
        longestCommonSubsequence(s1, s2)
        endRoutine()
    elif int(op) == 4:
        print("Insert first string")
        s1 = input("> ")
        print("Insert second string")
        s2 = input("> ")

        try:
            s1 = str(s1)
            s2 = str(s2)
        except ValueError:
            print("Please, insert valid string")
            continue
        longestCommonSubstring(s1, s2)
        endRoutine()
    else:
        print("Please select a valid operation!")
