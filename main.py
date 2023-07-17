import weights as w


# Matrix cell used for dynamic programming approach, contains value for alignment, direction for backtracking
class MatrixCell:
    value = 0
    backtracking = "DIAG"


# Print result of backtracking according to mode:
# GSA -> global sequence alignment
# LSA -> local sequence alignment
# LCS -> longest common subsequence
def backtracking(matrix, rowsNum, colsNum, string1, string2, mode):
    if mode == "GSA":
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

    elif mode == "LSA":
        currRow = rowsNum - 1
        currCol = colsNum - 1
        alignedString1 = ""
        alignedString2 = ""
        resultString = ""
        finalScore = 0

        currEl = matrix[currRow][currCol]
        for i in range(rowsNum):
            for j in range(colsNum):
                if matrix[i][j].value >= currEl.value:
                    currEl = matrix[i][j]
                    currRow = i
                    currCol = j

        while currEl.value != 0:
            if string1[currRow - 1] == string2[currCol - 1]:
                alignedString1 += string1[currRow - 1]
                alignedString2 += string2[currCol - 1]
                resultString += '*'
                finalScore += w.LSA_MATCH
            else:
                alignedString1 += string1[currRow - 1]
                alignedString2 += string2[currCol - 1]
                resultString += '|'
                finalScore += w.LSA_MISMATCH
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

    elif mode == "LCS":
        lcs = ""
        currRow = rowsNum - 1
        currCol = colsNum - 1
        currEl = matrix[currRow][currCol]

        while 1:
            if currRow == 0 and currCol == 0:
                break
            else:
                if currEl.backtracking == "UP":
                    currRow -= 1
                    currEl = matrix[currRow][currCol]
                elif currEl.backtracking == "LEFT":
                    currCol -= 1
                    currEl = matrix[currRow][currCol]
                elif currEl.backtracking == "DIAG":
                    lcs += string1[currRow - 1]
                    currRow -= 1
                    currCol -= 1
                    currEl = matrix[currRow][currCol]

        # Print result
        lcs = lcs[::-1]
        print("Longest common subsequence:", lcs)


# Assign direction given backtrack tuple
def assignDirection(backtrack):
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
    return direction


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
                matrix[i][j].backtracking = assignDirection(backtrack)

    # Backtracking
    backtracking(matrix, rowsNum, colsNum, string1, string2, "GSA")
    return


# Given two strings it returns local sequence alignment result
def localSequenceAlignment(st1, st2):
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
                    matrix[i][j].value = max(left + w.LSA_GAP, up + w.LSA_GAP, diag + w.LSA_MATCH, 0)
                else:
                    matrix[i][j].value = max(left + w.LSA_GAP, up + w.LSA_GAP, diag + w.LSA_MISMATCH, 0)

                backtrack = left, up, diag, 0
                matrix[i][j].backtracking = assignDirection(backtrack)

    # Backtracking
    backtracking(matrix, rowsNum, colsNum, string1, string2, "LSA")
    return


# Given two strings it returns the longest common subsequence shared by them (LCS weights are fixed)
def longestCommonSubsequence(st1, st2):
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
        matrix[i][0].value = 0 * i
        matrix[i][0].backtracking = "UP"
    for j in range(colsNum):
        matrix[0][j].value = 0 * j
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
                    matrix[i][j].value = max(left + 0, up + 0, diag + 1)
                else:
                    matrix[i][j].value = max(left + 0, up + 0, diag + -1)

                backtrack = left, up, diag
                matrix[i][j].backtracking = assignDirection(backtrack)

    # Backtracking
    backtracking(matrix, rowsNum, colsNum, string1, string2, "LCS")
    return


# TODO
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

        # TODO
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
