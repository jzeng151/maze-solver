from point import Point
from line import Line

class Cell():
  def __init__(self, win):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.visited = False
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self._win = win

  def draw(self):
    # top left bottom right
    # left: (x1, y1), (x1, y2)
    # right: (x,2, y1), (x2, y2)
    # top: (x1, y1), (x2, y1)
    # bottom: (x1, y2), (x2, y2)

    if self.has_left_wall:
      left_line = Line(Point(self._x1, self._y1,), Point(self._x1, self._y2))
      self._win.draw_line(left_line, fill_color="black")
    else:
      left_line = Line(Point(self._x1, self._y1, ), Point(self._x1, self._y2))
      self._win.draw_line(left_line, fill_color="white")
    if self.has_right_wall:
      right_line = Line(Point(self._x2, self._y1,), Point(self._x2, self._y2))
      self._win.draw_line(right_line, fill_color="black")
    else:
      right_line = Line(Point(self._x2, self._y1,), Point(self._x2, self._y2))
      self._win.draw_line(right_line, fill_color="white")
    if self.has_top_wall:
      top_line = Line(Point(self._x1, self._y1,), Point(self._x2, self._y1))
      self._win.draw_line(top_line, fill_color="black")
    else:
      top_line = Line(Point(self._x1, self._y1,), Point(self._x2, self._y1))
      self._win.draw_line(top_line, fill_color="white")
    if self.has_bottom_wall:
      bottom_line = Line(Point(self._x1, self._y2,), Point(self._x2, self._y2))
      self._win.draw_line(bottom_line, fill_color="black")
    else:
      bottom_line = Line(Point(self._x1, self._y2, ), Point(self._x2, self._y2))
      self._win.draw_line(bottom_line, fill_color="white")
    
  def draw_move(self, to_cell, undo=False):
    fill_color = "red"
    if undo:
      fill_color = "gray"
    mid_c1_x = abs(self._x1 + self._x2) // 2
    mid_c1_y = abs(self._y1 + self._y2) // 2
    mid_c2_x = abs(to_cell._x1 + to_cell._x2) // 2
    mid_c2_y = abs(to_cell._y1 + to_cell._y2) // 2
    p1 = Point(mid_c1_x, mid_c1_y)
    p2 = Point(mid_c2_x, mid_c2_y)
    line = Line(p1, p2)
    self._win.draw_line(line, fill_color)
