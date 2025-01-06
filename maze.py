import time
import random
from random import randrange

from cell import Cell

class Maze():
  def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win,
      seed = None
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols  = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self._cells = []
    self._win = win
    if seed:
      random.seed(seed)
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    self._reset_cells_visited()

  def _create_cells(self):
    for i in range(self.num_cols):
      col_cells = []
      for j in range(self.num_rows):
        col_cells.append(Cell(self._win))
      self._cells.append(col_cells)
    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self._draw_cells(i, j)

  def _draw_cells(self, i, j):
    if self._win is None:
      return
    cell = self._cells[i][j]
    cell._x1 = i * self.cell_size_x + self.x1
    cell._y1 = j * self.cell_size_y + self.y1
    cell._x2 = cell._x1 + self.cell_size_x
    cell._y2 = cell._y1 + self.cell_size_y
    cell.draw()
    self._animate()

  def _animate(self):
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    entrance_cell = self._cells[0][0]
    exit_cell = self._cells[self.num_cols-1][self.num_rows-1]
    entrance_cell.has_top_wall = False
    entrance_cell.draw()
    exit_cell.has_bottom_wall = False
    exit_cell.draw()

  def _break_walls_r(self, i, j):
    curr_cell = self._cells[i][j]
    curr_cell.visited = True
    while True:
      to_visit = []
      #check up [0,2]
      if i > 0 and not self._cells[i-1][j].visited:
        to_visit.append((i-1,j))
      #check right
      if j < self.num_rows-1 and not self._cells[i][j+1].visited:
        to_visit.append((i, j+1))
      #check down
      if i < self.num_cols-1 and not self._cells[i+1][j].visited:
        to_visit.append((i+1, j))
      #check left
      if j > 0 and not self._cells[i][j-1].visited:
        to_visit.append((i, j-1))
      if len(to_visit) == 0:
        return
      next_cell_i = randrange(0, len(to_visit), 1)
      next_i = to_visit[next_cell_i][0]
      next_j = to_visit[next_cell_i][1]
      next_cell = self._cells[next_i][next_j]
      del to_visit[next_cell_i]
      if next_i < i:
        curr_cell.has_left_wall = False
        next_cell.has_right_wall = False
      if next_j > j:
        curr_cell.has_bottom_wall = False
        next_cell.has_top_wall = False
      if next_i > i:
        curr_cell.has_right_wall = False
        next_cell.has_left_wall = False
      if next_j < j:
        curr_cell.has_top_wall = False
        next_cell.has_bottom_wall = False
      curr_cell.draw()
      next_cell.draw()
      self._animate()
      self._break_walls_r(next_i, next_j)

  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
        cell.visited = False
