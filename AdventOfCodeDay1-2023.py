if __name__ == '__main__':
    #Input of advent of code puzzle input
    filePath = r"C:\Users\stjle\Desktop\Advent of code\AdventOfCodeDay1.txt"
    puzzleInput = open(filePath)

    totalSum = 0

    for line in puzzleInput:
        rightmostDigit = -1
        leftmostDigit = -1
        lineSum = 0

        for character in line:
            if character.isdigit():
                if leftmostDigit == -1:
                    rightmostDigit = int(character)
                    leftmostDigit = int(character)
                else:
                    rightmostDigit = int(character)

        lineSum = (leftmostDigit * 10) + rightmostDigit
        totalSum += lineSum

    print(totalSum)

    puzzleInput.close()


