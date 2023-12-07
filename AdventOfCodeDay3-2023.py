def sumOfPartNumbers(filePath):

    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    engineSchematicMatrix = []

    for line in puzzleInput:
        row = []
        for item in line:
            row.append(item)
        engineSchematicMatrix.append(row)

    puzzleInput.close()

    gearLocations = {}

    for i in range(0, len(engineSchematicMatrix)):
        for j in range(0, len(engineSchematicMatrix[i])):
            if not engineSchematicMatrix[i][j].isdigit() and not engineSchematicMatrix[i][j].isspace() and engineSchematicMatrix[i][j] != ".":
                gearLocations["gear: " + str(i) + "," + str(j)] = identifyPartNumbers(engineSchematicMatrix, i, j)

    partSum = 0

    for key in gearLocations.keys():
        for item in gearLocations[key]:
            partSum += item

    return partSum

def sumOfGearRatios(filePath):
    try:
        puzzleInput = open(filePath)
    except FileNotFoundError:
        return "File Not Found"

    engineSchematicMatrix = []

    for line in puzzleInput:
        row = []
        for item in line:
            row.append(item)
        engineSchematicMatrix.append(row)

    puzzleInput.close()

    gearLocations = {}

    for i in range(0, len(engineSchematicMatrix)):
        for j in range(0, len(engineSchematicMatrix[i])):
            if engineSchematicMatrix[i][j] == "*":
                gearLocations["gear: " + str(i) + "," + str(j)] = identifyPartNumbers(engineSchematicMatrix, i, j)

    gearSum = 0

    for key in gearLocations.keys():

        if len(gearLocations[key]) == 2:

            currentGearRatio = 1

            for item in gearLocations[key]:
                currentGearRatio *= item

            gearSum += currentGearRatio

    return gearSum

def identifyPartNumbers(matrix, y, x):

    partNumbers = set()

    for i in range(-1, 2):
        for j in range(-1, 2):
            if matrix[y + i][x + j].isdigit():
                partNumbers.add(readPartNumber(matrix, y + i, x + j))

    return partNumbers

def readPartNumber(matrix, y, x):

    startingIndex = x

    while matrix[y][startingIndex].isdigit():
        startingIndex -= 1

    startingIndex += 1

    partNumber = int(matrix[y][startingIndex])

    while matrix[y][startingIndex + 1].isdigit():
        partNumber *= 10
        partNumber += int(matrix[y][startingIndex + 1])

        startingIndex += 1

    return partNumber

if __name__ == '__main__':

    # Input of advent of code puzzle input (Day 2)
    filePath = r"C:\Users\stjle\Desktop\Advent of code\AdventOfCodeDay3.txt"

    print(sumOfPartNumbers(filePath))
    print(sumOfGearRatios(filePath))
