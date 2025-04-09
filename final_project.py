######################################################################
# Author: Arbjosa Halilaj, Iuliia Likhacheva
# Username: halilaja, likhachevai
#
# PO1
#
# Purpose: To generate random mazes using the Turtle library with the timer and allow the user to solve it interactively using keyboard controls.
#
#######################################################################
# Acknowledgements:
####################################################################################

import time
import turtle
import math

class Point:
    def __init__(self, x=0, y=0):
        """
        Initializes a new Point object at coordinates (x, y).

        Args: x (float, optional): The x-coordinate. Defaults to 0.
              y (float, optional): The y-coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.turtle = None

    def __str__(self):
        """
        Returns a string representation of the Point object.

        Returns: str: The formatted string "Point(x, y)".
        """
        return f"Point({self.x}, {self.y})"

    def distance_from_origin(self):
        """
        Computes the Euclidean distance from the point to the origin (0, 0).

        Returns: float: The distance from the origin.
        """
        pass

    def user_set(self):
        """
        Allows the user to input and update the x and y coordinates of the Point.
        """
        pass

    def draw_point(self):
        """
        Uses the turtle graphics module to draw the point on the screen.
        """
        pass



class Navigator:
    def __init__(self, maze, start_x, start_y):
        """
        Initializes the Navigator with a starting position and a reference to the maze.

        Args: maze (Maze): The Maze object that the navigator will move through.
              start_x (int): The starting x-coordinate.
              start_y (int): The starting y-coordinate.
        """
        pass

    def move_forward(self):
        """
        Moves the navigator forward in the current facing direction.
        """
        pass

    def turn_left(self):
        """
        Rotates the navigator's current facing direction to the left.
        """
        pass

    def turn_right(self):
        """
        Rotates the navigator's current facing direction to the right.
        """
        pass

    def at_goal(self):
        """
        Checks if the navigator's current position is the goal cell of the maze.

        Returns: bool: True if the navigator is at the goal, False otherwise.
        """
        pass

    def get_time_elapsed(self):
        """
        Calculates the time elapsed since the navigator began moving through the maze.

        Returns: float: Time in seconds since navigation started.
        """
        pass

class Maze:
    def __init__(self, grid):
        """
        Initializes the Maze with a given grid layout.

        Args: grid: A 2D list representing the maze structure.
        """
        pass

    def is_path(self, x, y):
        """
        Checks whether the cell at position (x, y) is a valid walkable path.

        Args: x (int): The x-coordinate (column) of the cell.
              y (int): The y-coordinate (row) of the cell.

        Returns: bool: True if the cell is walkable (not a wall), False otherwise.
        """
        pass

    def get_start(self):
        """
        Returns the starting position of the maze.

        Returns: tuple[int, int]: The (x, y) coordinates of the starting position.
        """
        pass

    def get_goal(self):
        """
        Returns the goal position of the maze.

        Returns: tuple[int, int]: The (x, y) coordinates of the goal position.
        """
        pass

    def generate_maze(self, difficulty):
        """
        Generates a new maze layout based on the specified difficulty level.

        Args: difficulty (int): An integer indicating the desired complexity of the maze.
        """
        pass

class MazeDrawer:
    def __init__(self, maze):
        """
        Initializes the MazeDrawer with a reference to the maze object.

        :param maze (Maze): The maze object containing the grid to draw.
        """
        self.maze = maze
        self.turtle = None      #turtle object to draw maze
        self.cell_size = 20     #size of each cell in pixels

    def draw_maze(self):
        """
        Uses the turtle graphics module to draw the maze layout including walls and paths.
        """
        pass

    def draw_navigator(self, x, y):
        """
        Draws the navigator's starting position in the maze.
        :param x: x-coordinate in the maze grid.
        :param y: y-coordinate in the maze grid.
        """
        pass

    def update_position(self, x, y):
        """
        Moves the navigator to a new position in the maze.
        :param x: new x-coordinate in the maze grid.
        :param y: new y-coordinate in the maze grid.
        :return:
        """
        pass

class MazeGUI:
    def __init__(self):
        """
        Initializes the GUI window, timer, and related components for maze interaction.
        """
        self.window = None      #tkinter window instance
        self.difficulty = None  #selected difficulty level
        self.timer = None       #timer label
        self.navigator = None   #navigator object
        self.maze = None        #maze object

    def select_difficulty(self, level):
        """
        Sets the selected difficulty level and triggers maze generation.

        Args:
            level (str): Chosen difficulty level ("Easy", "Medium", or "Hard").
        """
        pass

    def start_timer(self):
        """
        Starts the timer to track how long the user takes to solve the maze.
        """
        pass

    def run(self):
        """
        Runs the Tkinter mainloop to display and maintain the GUI.
        """
        pass