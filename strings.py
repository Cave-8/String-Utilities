import weights as w


# Matrix cell used for dynamic programming approach, contains value for alignment, direction for backtracking
class MatrixCell:
    value = 0
    backtracking = "DIAG"


# Print result of backtracking according to mode:
# GSA -> global sequence alignment
# LSA -> local sequence alignment
# LCS-SEQ -> longest common subsequence
# LCS-ST -> longest common substring
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

    elif mode == "LCS-SEQ":
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
        if len(lcs) > 0:
            print("Longest common subsequence:", lcs)
        else:
            print("No common subsequence")

    elif mode == "LCS-ST":
        lcs = ""
        currRow = rowsNum - 1
        currCol = colsNum - 1
        currEl = matrix[0][0]

        for i in range(rowsNum):
            for j in range(colsNum):
                if matrix[i][j].value > currEl.value:
                    currEl = matrix[i][j]
                    currRow = i
                    currCol = j

        while 1:
            if currEl.value == 0:
                break
            else:
                lcs += string1[currRow-1]
                currEl = matrix[currRow-1][currCol-1]
                currRow -= 1
                currCol -= 1

        # Print result
        lcs = lcs[::-1]
        if len(lcs) > 0:
            print("Longest common substring:", lcs)
        else:
            print("No common substring")


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

    matrix = [[] for _ in range(rowsNum)]
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

    matrix = [[] for _ in range(rowsNum)]
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

    matrix = [[] for _ in range(rowsNum)]
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
    backtracking(matrix, rowsNum, colsNum, string1, string2, "LCS-SUB")
    return


# Given two strings it returns the longest common substring shared by them
# Can be optimized using suffix tree (from O(len1 * len2) to O(len1 + len2))
def longestCommonSubstring(st1, st2):
    string1 = str(st1).upper()
    string2 = str(st2).upper()
    rowsNum = len(string1) + 1
    colsNum = len(string2) + 1

    matrix = [[] for _ in range(rowsNum)]
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
                    matrix[i][j].value = max(0, diag + 1)
                else:
                    matrix[i][j].value = 0

                backtrack = left, up, diag
                matrix[i][j].backtracking = assignDirection(backtrack)

    # Backtracking
    backtracking(matrix, rowsNum, colsNum, string1, string2, "LCS-ST")
    return


# Left rotation of n spaces
def leftRotate(st, n):
    return st[n:] + st[:n]


# Burrows-Wheelers encoder
def burrowsWheelerEncoder(st1):
    st1 += "$"
    stringToReturn = ""
    array = []

    for i in range(len(st1)):
        if i != 0:
            st1 = leftRotate(st1, 1)
        array.append(st1)

    array.sort()

    for i in range(len(st1)):
        stringToReturn += array[i][len(st1) - 1]

    print("BWT of given string is:")
    print(stringToReturn)


# Burrows-Wheelers decoder using FM index -> can be optimized
def burrowsWheelerDecoder(st1):
    cTab = []
    LF = []
    fIndex = sorted(st1)
    lIndex = list(st1)
    alphabet = []
    toBeReturned = list()

    class C_Cell:
        letter = ''
        posOcc = 0

    currChar = ''
    numChar = 0

    # C(c) building
    for i in range(len(st1)):
        if fIndex[i] != currChar:
            currChar = fIndex[i]
            cTab.append(C_Cell())
            cTab[numChar].letter = currChar
            cTab[numChar].posOcc = i
            alphabet.append(currChar)
            numChar += 1

    # Occurrences table building
    alphabet = sorted(alphabet)
    occTable = [[] for _ in range(len(alphabet))]

    for i in range(len(alphabet)):
        for j in range(len(st1)):
            occTable[i].append(0)

    for i in range(len(alphabet)):
        for j in range(len(st1)):
            if alphabet[i] == st1[j]:
                if j != 0:
                    occTable[i][j] = occTable[i][j - 1] + 1
                else:
                    occTable[i][j] = 1
            else:
                occTable[i][j] = occTable[i][j - 1]

    ind = 0
    for i in range(len(st1)):
        for j in range(len(cTab)):
            if st1[i] == cTab[j].letter:
                ind = j
                break
        LF.append(cTab[ind].posOcc + occTable[ind][i])

    for i in range(len(LF)):
        LF[i] -= 1

    toBeReturned.append('$')
    fRow = lIndex.index('$')
    for i in range(len(lIndex)):
        fRow = LF[fRow]
        if lIndex[fRow] != '$':
            toBeReturned.append(lIndex[fRow])

    toBeReturned = ''.join(toBeReturned)
    toBeReturned = toBeReturned[::-1]
    print(toBeReturned)


# Main body
while 1:
    print("Please select operation:")
    print("1 - Global sequence alignment")
    print("2 - Local sequence alignment")
    print("3 - Longest common subsequence")
    print("4 - Longest common substring")
    print("5 - Burrows-Wheeler transform")
    print("6 - Exit")

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
            print("Do you want to perform string to BWT (1) or vice-versa (2)?")
            choice = input("> ")
            try:
                if int(choice) == 1:
                    print(
                        "Insert string without terminator character ($), terminator character is AUTOMATICALLY appended!")
                    s1 = input("> ")
                    try:
                        s1 = str(s1)
                    except ValueError:
                        print("Please, insert valid string")
                        continue
                    burrowsWheelerEncoder(s1)
                elif int(choice) == 2:
                    print("Insert BWT (be sure that terminator character $ is included)")
                    s1 = input("> ")
                    try:
                        s1 = str(s1)
                    except ValueError:
                        print("Please, insert valid string")
                        continue
                    burrowsWheelerDecoder(s1)
            except ValueError:
                print("Please, insert valid string")
                continue

        elif int(op) == 6:
            print("Goodbye!")
            exit(0)

        else:
            print("Please select a valid operation!")
    except ValueError:
        print("Please select a valid operation!")
