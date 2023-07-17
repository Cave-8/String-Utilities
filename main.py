import numpy as np
import weights as w


# Matrix cell used for dynamic programming approach, contains value for alignment, direction for backtracking
class MatrixCell:
    value = 0
    backtracking = "DIAG"


# Given two strings it returns global sequence alignment result
def globalSequenceAlignment(st1, st2):
    string1 = str(st1).upper()
    string2 = str(st2).upper()
    rowsNum = len(string1) + 1
    colsNum = len(string2) + 1

    matrix = [[] for i in range(rowsNum)]
    for i in range(rowsNum):
        for j in range(colsNum):
            matrix[i].append(MatrixCell())

    # Matrix initialization
    for i in range(rowsNum):
        matrix[i][0].value = w.GSA_GAP * i
        matrix[i][0].backtracking = "UP"
    for j in range(colsNum):
        matrix[0][j].value = w.GSA_GAP * j
        matrix[0][j].backtracking = "LEFT"

    for i in range(rowsNum):
        for j in range(colsNum):
            if i == 0 or j == 0:
                continue
            else:
                left = matrix[i][j - 1].value
                up = matrix[i - 1][j].value
                diag = matrix[i - 1][j - 1].value
                if string1[i - 1] == string2[j - 1]:
                    matrix[i][j].value = max(left + w.GSA_GAP, up + w.GSA_GAP, diag + w.GSA_MATCH)
                else:
                    matrix[i][j].value = max(left + w.GSA_GAP, up + w.GSA_GAP, diag + w.GSA_MISMATCH)

                backtrack = left, up, diag
                direction = "?"
                currVal = float('-inf')
                for b in range(len(backtrack)):
                    if backtrack[b] >= currVal:
                        currVal = backtrack[b]
                        if b == 0:
                            direction = "LEFT"
                        elif b == 1:
                            direction = "UP"
                        else:
                            direction = "DIAG"
                matrix[i][j].backtracking = direction

    # Begin backtracking
    currEl = matrix[rowsNum - 1][colsNum - 1]
    currRow = rowsNum - 1
    currCol = colsNum - 1
    alignedString1 = ""
    alignedString2 = ""
    resultString = ""
    finalScore = 0
    while 1:
        if currRow == 0 and currCol == 0:
            break
        else:
            if currEl.backtracking == "UP":
                finalScore += w.GSA_GAP
                resultString += ' '
                alignedString1 += string1[currRow - 1]
                alignedString2 += '_'
                currRow -= 1
                currEl = matrix[currRow][currCol]
            elif currEl.backtracking == "LEFT":
                finalScore += w.GSA_GAP
                resultString += ' '
                alignedString1 += '_'
                alignedString2 += string2[currCol - 1]
                currCol -= 1
                currEl = matrix[currRow][currCol]
            elif currEl.backtracking == "DIAG":
                if string1[currRow - 1] != string2[currCol - 1]:
                    finalScore += w.GSA_MISMATCH
                    resultString += '|'
                else:
                    finalScore += w.GSA_MATCH
                    resultString += '*'
                alignedString1 += string1[currRow - 1]
                alignedString2 += string2[currCol - 1]
                currRow -= 1
                currCol -= 1
                currEl = matrix[currRow][currCol]

    # Print result
    alignedString1 = alignedString1[::-1]
    alignedString2 = alignedString2[::-1]
    resultString = resultString[::-1]

    print(alignedString1)
    print(resultString)
    print(alignedString2)
    print("Score:", finalScore)
    return


# Given two strings it returns local sequence alignment result
def localSequenceAlignment(st1, st2):
    print("Test")
    string1 = str(st1)
    string2 = str(st2)


# Given two strings it returns the longest common subsequence shared by them
def longestCommonSubsequence(st1, st2):
    print("Test")
    string1 = str(st1)
    string2 = str(st2)


# Given two strings it returns the longest common substring shared by them
def longestCommonSubstring(st1, st2):
    print("Test")
    string1 = str(st1)
    string2 = str(st2)

# Main body
while 1:
    print("Please select operation:")
    print("1 - Global sequence alignment")
    print("2 - Local sequence alignment")
    print("3 - Longest common subsequence")
    print("4 - Longest common substring")
    print("5 - Exit")

    try:
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

        elif int(op) == 5:
            print("Goodbye!")
            exit(0)

        else:
            print("Please select a valid operation!")
    except ValueError:
        print("Please select a valid operation!")
