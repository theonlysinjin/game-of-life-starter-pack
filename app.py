import helper, time

def tick(grid):
  ##               ##
  ## DO LOGIC HERE ##
  ##               ##
  # Example Code
  currentTick = globals()["ticks"]
  if (currentTick < len(grid)):
    grid[currentTick][currentTick] = True
  ##               ##

  return grid


def updateGrid(newGrid):
  globals()["mainGrid"] = newGrid
  return newGrid

if __name__ == '__main__':
  global mainGrid
  global gridSize
  global ticks
  gridSize = 30
  timeBetweenTicks = 1

  emptyGrid = helper.makeGrid(gridSize, gridSize)
  starterGrid = helper.generateStart(emptyGrid)
  mainGrid = updateGrid(starterGrid)
  ticks = 0

  print("Starting with grid sized %sx%s" %(gridSize, gridSize))
  helper.printGrid(ticks, starterGrid)
  time.sleep(timeBetweenTicks)

  while True:
    ticks += 1

    mainGrid = tick(mainGrid)
    helper.printGrid(ticks, mainGrid)

    time.sleep(timeBetweenTicks)
