def calibrationNums (filePath):

    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    totalSum = 0

    for line in puzzleInput:
        rightmostDigit = -1
        leftmostDigit = -1
        lineSum = 0

        for character in line:
            if character.isdigit():
                leftmostDigit, rightmostDigit = updateDigits(leftmostDigit, rightmostDigit, int(character))

        lineSum = (leftmostDigit * 10) + rightmostDigit
        totalSum += lineSum

    puzzleInput.close()

    return totalSum

def calibrationNumsWithWords (filepath):

    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    totalSum = 0

    wordToNum = {"one" : 1,
                 "two" : 2,
                 "three" : 3,
                 "four" : 4,
                 "five" : 5,
                 "six" : 6,
                 "seven" : 7,
                 "eight" : 8,
                 "nine" : 9}

    for line in puzzleInput:
        rightmostDigit = -1
        leftmostDigit = -1
        lineSum = 0

        for i in range(0, len(line)):

            if i >= 4 and line[i - 4: i + 1] in wordToNum.keys():
                leftmostDigit, rightmostDigit = updateDigits(leftmostDigit, rightmostDigit, wordToNum[line[i - 4: i + 1]])
            elif i >= 3 and line[i - 3: i + 1] in wordToNum.keys():
                leftmostDigit, rightmostDigit = updateDigits(leftmostDigit, rightmostDigit, wordToNum[line[i - 3: i + 1]])
            elif i >= 2 and line[i - 2: i + 1] in wordToNum.keys():
                leftmostDigit, rightmostDigit = updateDigits(leftmostDigit, rightmostDigit, wordToNum[line[i - 2: i + 1]])
            elif line[i].isdigit():
                leftmostDigit, rightmostDigit = updateDigits(leftmostDigit, rightmostDigit, int(line[i]))

        lineSum = (leftmostDigit * 10) + rightmostDigit
        totalSum += lineSum

    puzzleInput.close()

    return totalSum

def updateDigits(leftmostDigit, rightmostDigit, currentDigit):
    if leftmostDigit == -1:
        rightmostDigit = currentDigit
        leftmostDigit = currentDigit
    else:
        rightmostDigit = currentDigit

    return leftmostDigit, rightmostDigit


if __name__ == '__main__':
    # Input of advent of code puzzle input
    filePath = r"C:\Users\stjle\Desktop\Advent of code\AdventOfCodeDay1.txt"

    print(calibrationNums(filePath))
    print(calibrationNumsWithWords(filePath))


