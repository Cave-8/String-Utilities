# Given two strings it returns global sequence alignment result
def globalSequenceAlignment(s1, s2):
    print("Test")


# Given two strings it returns local sequence alignment result
def localSequenceAlignment(s1, s2):
    print("Test")


# Given two strings it returns the longest common subsequence shared by them
def longestCommonSubsequence(s1, s2):
    print("Test")


# Given two strings it returns the longest common substring shared by them
def longestCommonSubstring(s1, s2):
    print("Test")


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
    op = input("> ")

    if int(op) == 1:

        endRoutine()
    elif int(op) == 2:

        endRoutine()
    elif int(op) == 3:

        endRoutine()
    elif int(op) == 4:

        endRoutine()
    else:
        print("Please select a valid operation!")
