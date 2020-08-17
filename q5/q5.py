#read input
l = int(input())
n = int(input())
tiles = []
for x in range(n):
    numAndColor = input().split()
    numAndColor[0] = int(numAndColor[0])
    tiles.append(numAndColor)

#sorting
def sortNum(e):
    return e[0]
tiles.sort(key=sortNum, reverse=True)

#generate table
table = []
for r in range(l):
    row = []
    for c in range(l):
        row.append("_")
    table.append(row)

#jumping logic
isFirstRound = True
def makeAJump(r, c):
    global isFirstRound
    newR = r
    newC = c + 2
    if newC >= l:
        newR += 1
        if newR >= l:
            newR = 0
            isFirstRound = False
        if isFirstRound:
            if newR % 2 == 0:
                newC = 0
            else:
                newC = 1
        else:
            if newR % 2 == 0:
                newC = 1
            else:
                newC = 0
    return newR, newC

#fill the table
currentR, currentC = 0, 0
for colorIndex in range(n):
    colorCount = tiles[colorIndex][0]
    colorCode = tiles[colorIndex][1]
    for i in range(colorCount):
        table[currentR][currentC] = colorCode
        currentR, currentC = makeAJump(currentR, currentC)

#print the table
for r in range(l):
    for c in range(l):
        if c != 0:
            print(" ", end="")
        print(table[r][c], end="")
    print("")
