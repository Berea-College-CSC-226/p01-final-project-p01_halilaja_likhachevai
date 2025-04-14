######################################################################
# Author: Arbjosa Halilaj, Iuliia Likhacheva
# Username: halilaja, likhachevai
#
# Assignment: P01: Final Project
#
# Purpose: To generate random mazes using the Turtle library with the timer and allow the user to solve it interactively using keyboard controls.
#
#######################################################################
# Acknowledgements:
#######################################################################

import time
import turtle
import math
import tkinter as tk
import random


class Point:
    def __init__(self, x=0, y=0):
        """
        Initializes a new Point object at coordinates (x, y).

        Args: x (float, optional): The x-coordinate. Defaults to 0.
              y (float, optional): The y-coordinate. Defaults to 0.
        """
        self.x = x #instance variable which holds the x value
        self.y = y #instance variable which holds the y value
        self.turtle = None #instance variable which is initially set to None until draw_point() is called.

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
        return math.sqrt(self.x ** 2 + self.y ** 2)

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
    def __init__(self, maze, x=0, y=0, direction='N'):
        """
        Initializes the Navigator with a starting position and a reference to the maze.

        Args: maze (Maze): The Maze object that the navigator will move through.
              start_x (int): The starting x-coordinate.
              start_y (int): The starting y-coordinate.
        """
        self.x = x #instance variable which holds the x coordinate
        self.y = y #instance variable which holds the y coordinate
        self.direction = direction #instance variable for current facing direction
        self.maze = maze #instance variable that holds reference to Maze
        self.timer_start = None #timestamp when navigator begins

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
        if self.timer_start is None:
            self.timer_start = time.time()
            return 0
        return time.time() - self.timer_start

class Maze:
    def __init__(self, grid=None):
        """
        Initializes the Maze with a given grid layout.

        Args: grid: A 2D list representing the maze structure.
        """
        self.grid = grid if grid else [[0, 1], [1, 0]] #2D list representing the maze layout
        self.start = (0, 0) #starting position
        self.goal = (1, 1) #goal position
        self.difficulty = None #current difficulty level

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
        return self.start

    def get_goal(self):
        """
        Returns the goal position of the maze.

        Returns: tuple[int, int]: The (x, y) coordinates of the goal position.
        """
        return self.goal

    def find_start_position(grid):
        """
        Searches the maze grid for the cell marked as the starting point ('S')
        Args: grid (list[list[str]]): the 2d maze grid
        :return: tuple[int, int]: coordinates (x,y) of the starting cell, or None if not found
        """
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return x, y
        return None

    def generate_maze(self, difficulty):
        """
        Generates a new maze layout based on the specified difficulty level.

        Args: difficulty (int): An integer indicating the desired complexity of the maze.
        """

        # Map difficulty levels to grid sizes
        size_map = {"Easy": 10, "Medium": 20, "Hard": 30}

        # Get size based on selected difficulty
        size = size_map.get(difficulty)

        self.grid = [] # Create an empty grid
        for i in range(size):
            row = [] # Create an empty row
            for j in range(size):
                row.append('#') # Add a wall to the row
            self.grid.append(row) # Add the row to the grid


        # Loop through only odd coordinates (skip every second cell to leave space for walls between paths)
        for y in range(1, size, 2):
            for x in range(1, size, 2):
                self.grid[y][x] = ' ' # Make the cell a path

                directions = []
                if x > 1:
                    directions.append((-1, 0))  # Option to carve west
                if y > 1:
                    directions.append((0, -1))  # Option to carve north


                # If at least one direction is valid, carve a passage
                if directions:
                    dx, dy = random.choice(directions)
                    self.grid[y + dy][x + dx] = ' ' # Remove wall between current and chosen cell

        self.start = (1, 1) # Start
        self.goal = (size - 2, size - 2) # Goal

        # Mark start and goal in the grid for drawing later
        self.grid[self.start[1]][self.start[0]] = 'S'
        self.grid[self.goal[1]][self.goal[0]] = 'G'

        self.difficulty = difficulty

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
        turtle.clearscreen()
        turtle.speed(0.1)
        turtle.hideturtle()
        turtle.penup()

        # Center maze horizontally: move left by half its width in pixels
        start_x = -len(self.maze.grid[0]) * self.cell_size // 2

        # Center maze vertically: move down by half its height in pixels
        start_y = len(self.maze.grid) * self.cell_size // 2


        # Loop over every row and cell in the 2D maze grid
        for y, row in enumerate(self.maze.grid): # enumerate helps to loop through a list while also keeping track of the index.
            for x, cell in enumerate(row):
                # Convert grid coordinates to screen (pixel) coordinates
                screen_x = start_x + x * self.cell_size
                screen_y = start_y - y * self.cell_size

                turtle.goto(screen_x, screen_y) # Move turtle to the top-left corner of the cell

                if cell == '#':
                    turtle.fillcolor("black") # Wall
                elif cell == ' ':
                    turtle.fillcolor("white") # Path
                elif cell == 'S':
                    turtle.fillcolor("green") # Start
                elif cell == 'G':
                    turtle.fillcolor("red") # Goal

                turtle.begin_fill()
                for i in range(4): # Draws a square
                    turtle.pendown()
                    turtle.forward(self.cell_size)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()

        turtle.done()

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
        self.window = None      #will be initialized in select_difficulty
        self.difficulty = None  #selected difficulty level
        self.timer = None       #timer label (not used yet)
        self.navigator = None   #navigator object
        self.maze = None        #maze object

    def show_welcome_window(self):
        """
        Displays a welcome window before selecting difficulty.
        """
        welcome = tk.Tk()
        welcome.title("Welcome to Turtle Escape")
        welcome.geometry("350x250")
        welcome.resizable(False, False)

        label = tk.Label(welcome, text="🐢 Welcome to Turtle Escape! 🐢", font=("Arial", 14))
        label.pack(pady=15)

        instructions = tk.Label(
            welcome,
            text="Navigate the turtle through the maze.\n Let's begin the adventure!",
            font=("Arial", 10),
            justify="center"
        )
        instructions.pack(pady=5)

        start_button = tk.Button(welcome, text="Start Game", command=welcome.destroy)
        start_button.pack(pady=10)

        welcome.mainloop()


    def set_difficulty(self, level):
        """
        Callback function to store the selected difficulty and close the window.
        :param level: Chosen difficulty level ("Easy", "Medium", or "Hard").
        :return:
        """
        self.difficulty = level #I.D.1
        self.window.destroy()   #I.D.2

        # Create a new window to display the selection
        result_window = tk.Tk()
        result_window.title("Selection")
        result_window.geometry("300x100")

        result_label = tk.Label(result_window, text=f"You selected: {self.difficulty}", font=("Arial", 14))
        result_label.pack(pady=20)

        ok_button = tk.Button(result_window, text="OK", command=result_window.destroy)
        ok_button.pack(pady=5)

        result_window.mainloop()

    def select_difficulty(self):
        """
        Displays a GUI window allowing the user to choose the maze difficulty.
        """
        self.window = tk.Tk()                                   #I.A.1
        self.window.title("Turtle Escape - Select Difficulty")  #I.A.2
        self.window.geometry("300x200")
        self.window.resizable(False, False)

        label = tk.Label(self.window, text= "Choose a difficulty level", font= ("Arial", 14))   #I.A.3
        label.pack(pady=20)

        easy_button = tk.Button(self.window, text= "Easy", width= 15,command= lambda: self.set_difficulty("Easy"))   #I.B.1/2
        medium_button = tk.Button(self.window, text= "Medium", width= 15, command= lambda: self.set_difficulty("Medium"))
        hard_button = tk.Button(self.window, text= "Hard", width= 15, command= lambda: self.set_difficulty("Hard"))

        easy_button.pack(pady=5)    #I.B.3
        medium_button.pack(pady=5)
        hard_button.pack(pady=5)

        self.window.mainloop()  #I.C.1/2

    def start_timer(self):
        """
        Starts the timer to track how long the user takes to solve the maze.
        """
        pass

    def run(self):
        """
        Runs the Tkinter mainloop to display and maintain the GUI.
        """
        self.maze = Maze()
        self.maze.generate_maze(self.difficulty)
        drawer = MazeDrawer(self.maze)
        drawer.draw_maze()

if __name__ == "__main__":
    gui = MazeGUI()
    gui.show_welcome_window()
    gui.select_difficulty()
    maze = Maze()
    maze.generate_maze(gui.difficulty)
    gui.run()