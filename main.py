from window import Window
from maze import Maze

def main():
  win = Window(800, 600)

  m = Maze(1, 1, 5, 5, 55, 55, win)

  win.wait_for_close()
  
if __name__ == "__main__":
  main()