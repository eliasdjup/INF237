

rows, columns = map(int, input().split())

waterSources = []
resultPicture = []

for row in range(rows):
    column = input()
    resultPicture.append(list(column))
    
    for i, e in list(enumerate(column)):
        if (e == "V"): 
            waterSources.append((row,i))


def simulateWater(x, y):
    if x < rows-1:

        if resultPicture[x+1][y] == ".":
            resultPicture[x+1][y] = "V"
            simulateWater(x+1,y)

        elif resultPicture[x+1][y] == "#":

            if (y > 0 and resultPicture[x][y-1] == "."):
                resultPicture[x][y-1] = "V"
                simulateWater(x,y-1)

            if (y < columns-1 and resultPicture[x][y+1] == "."):
                resultPicture[x][y+1] = "V"
                simulateWater(x,y+1)


for (x, y) in waterSources:
    simulateWater(x, y)

for i in resultPicture:
    print(''.join(i))




