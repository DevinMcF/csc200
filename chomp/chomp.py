from gasp import *

GRID_SIZE = 30                     # This sets size of everything
MARGIN = GRID_SIZE                 # How much space to leave round edge

BACKGROUND_COLOR = color.BLACK     # Colors we use
WALL_COLOR = (0.6 * 255, 0.9 * 255, 0.9 * 255)

# The shape of the maze.  Each character
# represents a different type of object
#   % - Wall
#   . - Food
#   o - Capsule
#   G - Ghost
#   P - Chomp
# Other characters are ignored

the_layout = [
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",     # There are 31 '%'s in this line
  "%.....%.................%.....%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.%.....%......%......%.....%.%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%.%%%.%.%%% %%%.%.%%%.%...%",
  "%.%%%.......%GG GG%.......%%%.%",
  "%...%.%%%.%.%%%%%%%.%.%%%.%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%.%.....%......%......%.....%.%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.....%........P........%.....%",
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"]


class Immovable:
    pass

class Nothing(Immovable):
    pass

class Maze:
    def __init__(self):
        self.have_window = False        # We haven't made window yet
        self.game_over = False          # Game isn't over yet
        self.set_layout(the_layout)     # Make all objects
        set_speed(20)                   # Set loop rate to 20 loops per second

    def set_layout(self, layout):
        height = len(layout)  # Length of list
        width = len(layout[0])  # Length of first string
        self.make_window(width, height)
        self.make_map(width, height)  # Start new map

        max_y = height - 1
        for x in range(width):  # Go through whole layout
            for y in range(height):
                char = layout[max_y - y][x]  # See discussion 1 page ago
                self.make_object((x, y), char)  # Create object

    def make_window(self, width, height):
        grid_width = (width-1) * GRID_SIZE     # Work out size of window
        grid_height = (height-1) * GRID_SIZE
        screen_width = 2*MARGIN + grid_width
        screen_height = 2*MARGIN + grid_height
        begin_graphics(screen_width,           # Create window
                       screen_height,
                       "Chomp",
                       BACKGROUND_COLOR)

    def to_screen(self, point):
        (x, y) = point
        x = x*GRID_SIZE + MARGIN     # Work out coordinates of point
        y = y*GRID_SIZE + MARGIN     # on screen
        return (x, y)

    def make_map(self, width, height):
        self.width = width  # Store size of layout
        self.height = height
        self.map = []  # Start with empty list
        for y in range(height):
            new_row = []  # Make new row list
            for x in range(width):
                new_row.append(Nothing())  # Add entry to list
            self.map.append(new_row)  # Put row in map

    def make_object(self, vector, char):
        pass

    def play(self):
        pass

    def finished(self):
        pass

    def done(self):
        pass


class Wall:
    pass


class Food:
    pass


class Capsule:
    pass


class Movable:
    pass


class Chomp:
    pass


class Ghost:
    pass


the_maze = Maze()

while not the_maze.finished():
    the_maze.play()

the_maze.done()

