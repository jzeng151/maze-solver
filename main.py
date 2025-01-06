from random import randrange
from window import Window
from maze import Maze

def main():
  win = Window(800, 600)
  seed = randrange(0, 9999, 1)
  m = Maze(1, 1, 5, 5, 55, 55, win, seed)
  m._solve()

  win.wait_for_close()
  
if __name__ == "__main__":
  main()