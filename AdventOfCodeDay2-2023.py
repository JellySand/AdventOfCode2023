import re

def sumOfGameValidator(filePath):

    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    maxColorNums = {"red" : 12,
                    "green" : 13,
                    "blue" : 14}

    validLineSum = 0

    for line in puzzleInput:

        lineTerms = re.findall(r'\w+', line)
        lineNum = 0

        for i in range(1, len(lineTerms)):
            leftTerm = lineTerms[i - 1]
            rightTerm = lineTerms[i]

            if leftTerm == "Game":
                lineNum = int(rightTerm)

            if rightTerm == "red" and int(leftTerm) > maxColorNums["red"]:
                lineNum = 0
                break
            elif rightTerm == "blue" and int(leftTerm) > maxColorNums["blue"]:
                lineNum = 0
                break
            elif rightTerm == "green" and int(leftTerm) > maxColorNums["green"]:
                lineNum = 0
                break

        validLineSum += lineNum

    puzzleInput.close()

    return validLineSum

def sumOfGameMinimumCubePossible(filePath):

    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    minimumCubeSum = 0

    for line in puzzleInput:

        lineTerms = re.findall(r'\w+', line)

        minimumRedCount = 0
        minimumBlueCount = 0
        minimumGreenCount = 0

        for i in range(1, len(lineTerms)):
            leftTerm = lineTerms[i - 1]
            rightTerm = lineTerms[i]

            if rightTerm == "red" and int(leftTerm) > minimumRedCount:
                minimumRedCount = int(leftTerm)
            elif rightTerm == "blue" and int(leftTerm) > minimumBlueCount:
                minimumBlueCount = int(leftTerm)
            elif rightTerm == "green" and int(leftTerm) > minimumGreenCount:
                minimumGreenCount = int(leftTerm)

        minimumCubeSum += (minimumRedCount * minimumBlueCount * minimumGreenCount)

    puzzleInput.close()

    return minimumCubeSum



if __name__ == '__main__':
    # Input of advent of code puzzle input (Day 2)
    filePath = r"C:\Users\stjle\Desktop\Advent of code\AdventOfCodeDay2.txt"

    print(sumOfGameValidator(filePath))
    print(sumOfGameMinimumCubePossible(filePath))
