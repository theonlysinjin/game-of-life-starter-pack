def makeGrid(x, y):
  actualX = x-1
  actualY = y-1
  theGrid = [[False for _ in range(actualY)] for _ in range(actualX)]
  return theGrid

def generateStart(grid):
  rowCount = len(grid)
  colCount = len(grid[0])
  halfRows = round(rowCount / 2)
  halfCols = round(colCount / 2)

  # Lower Row
  grid[halfRows+1][halfCols-1] = True
  grid[halfRows+1][halfCols] = True
  grid[halfRows+1][halfCols+1] = True
  # Mid Row
  grid[halfRows][halfCols+1] = True
  # Top Row
  grid[halfRows-1][halfCols] = True

  return grid

def printGrid(ticks, newGrid):
  print("- - -")
  print("Ticks: %s" %(ticks))
  print("- - -")

  for row in range(0, len(newGrid)):
    for col in range(0, len(newGrid[row])):
      if (newGrid[row][col]):
        newGrid[row][col] = 1
      else:
        newGrid[row][col] = ""

  for row in newGrid:
    format_row = "{:>3}" * (len(row) + 1)
    print(format_row.format("", *row))

  print("")


