import time
from cell import Cell
from point import Point

class Maze():
  def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols  = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self._cells = []
    self._win = win
    self._create_cells()

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
    time.sleep(0.1)
