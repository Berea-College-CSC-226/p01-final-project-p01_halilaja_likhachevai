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
import tkinter as tk
import random
import math
import importlib


should_restart = True

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

        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("blue")
        self.turtle.penup()
        self.set_heading()

        self.screen = turtle.Screen()
        self.timer_writer = turtle.Turtle()
        self.timer_writer.hideturtle()
        self.timer_writer.penup()
        self.timer_writer.goto(200, 200)
        self.is_timer_running = False


    def set_heading(self):
        """
        Sets the turtle's heading based on the current direction.

        Defaults to 90 degrees (North) if the direction is unrecognized.
        """
        headings = {'N': 0, 'E': 0, 'S': 270, 'W': 180}
        self.turtle.setheading(headings.get(self.direction, 90))


    def go_to_start(self):
        """
        Moves the turtle to the screen coordinates corresponding to the navigator's
        starting position in the maze grid.
        :return: None
        """
        cell_size = 20
        grid = self.maze.grid
        start_x = -len(grid[0]) * cell_size // 2
        start_y = len(grid) * cell_size // 2
        screen_x = start_x + self.x * cell_size + cell_size // 2
        screen_y = start_y - self.y * cell_size - cell_size // 2
        self.turtle.goto(screen_x, screen_y)
        self.turtle.showturtle()
        turtle.update()


    def move_forward(self):
        """
        Moves the navigator forward in the current facing direction.
        """

        # Starts the timer and begins updating if not already running.
        if not self.is_timer_running:
            self.timer_start = time.time()
            self.is_timer_running = True
            self.update_timer()

        move_offsets = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        dx, dy = move_offsets[self.direction]
        new_x, new_y = self.x + dx, self.y + dy

        # Convert navigator's position to grid coordinates (#47)
        if self.maze.is_path(new_x, new_y):  # Check if next cell is valid path (#48)
            self.x, self.y = new_x, new_y
            self.update_position()
        else:
            tk.messagebox.showwarning("Invalid Move", "You can't go through walls!")
            return  # Don't check goal or show popup if invalid move

        # Only trigger popup *if goal is reached*
        if self.at_goal():
            elapsed = self.get_time_elapsed()
            self.is_timer_running = False #stop timer loop
            self.timer_writer.goto(200,170)
            self.timer_writer.write(f"🎉 Goal reached in {elapsed:.1f} seconds!", font = ("Arial", 14, "bold"))
            self.show_end_popup(elapsed)  # Moved inside the if block


    def move_up(self):
        """
        Moves the navigator up
        """
        self.direction = 'N'
        self.move_forward()


    def move_down(self):
        """
        Moves the navigator down
        """
        self.direction = 'S'
        self.move_forward()


    def turn_left(self):
        """
        Rotates the navigator's current facing direction to the left.
        """
        self.direction = 'W'
        self.move_forward()


    def turn_right(self):
        """
        Rotates the navigator's current facing direction to the right.
        """
        self.direction = 'E'
        self.move_forward()

    def update_position(self):
        """
        Updates the turtle's screen position based on its current grid coordinates.

        Converts the navigator's (x, y) position in the maze grid to pixel coordinates
        on the screen and moves the turtle to that location. Also refreshes the turtle display.
        """
        cell_size = 20
        start_x = -len(self.maze.grid[0]) * cell_size // 2
        start_y = len(self.maze.grid) * cell_size // 2
        screen_x = start_x + self.x * cell_size + cell_size // 2
        screen_y = start_y - self.y * cell_size - cell_size // 2
        self.turtle.goto(screen_x, screen_y)
        turtle.update()


    def update_timer(self):
        """
        Continuously updates the on-screen timer while the navigator is moving.

        Displays the elapsed time since the navigator started and schedules the next update
        every 100 milliseconds using `ontimer`, as long as the timer is running.
        """
        if not self.is_timer_running:
            return
        elapsed = time.time() - self.timer_start # Calculates time elapsed since the timer started.
        self.timer_writer.clear()
        self.timer_writer.write(f"⏱️ Time: {elapsed:.1f} sec", font=("Arial", 14, "bold"))
        self.screen.ontimer(self.update_timer, 100)  # update every 100ms


    def bind_keys(self):
        """
        Binds arrow key inputs to navigator movement functions.

        Allows the user to control the navigator using the keyboard
        """
        turtle.listen()  # IV.B.2
        turtle.onkey(self.move_up, 'Up')
        turtle.onkey(self.move_down, 'Down')
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.turn_right, 'Right')


    def at_goal(self):
        """
        Checks if the navigator's current position is the goal cell of the maze.

        Returns: bool: True if the navigator is at the goal, False otherwise.
        """
        goal_x, goal_y = self.maze.get_goal()
        return self.x == goal_x and self.y == goal_y


    def start_timer(self):
        """
        Starts the timer to track how long the user takes to solve the maze.
        """
        if self.timer_start is None:
            self.timer_start = time.time()


    def get_time_elapsed(self):
        """
        Calculates the time elapsed since the navigator began moving through the maze.

        Returns: float: Time in seconds since navigation started.
        """
        if self.timer_start is None:
            self.timer_start = time.time()
            return 0
        return time.time() - self.timer_start

    def show_end_popup(self, elapsed):
        """
        Displays a popup window with 'Play Again' and 'Exit' buttons after completing the maze.
        """
        popup = tk.Tk()
        popup.title("Maze Completed!")
        popup.geometry("300x150")
        popup.resizable(False, False)

        label = tk.Label(popup, text=f"🎉 You solved the maze in {elapsed:.1f} seconds!", font=("Arial", 12))
        label.pack(pady=15)

        def play_again():
            """
            Restarts the game from the difficulty selection screen.
            """
            global should_restart
            should_restart = True
            popup.destroy()
            turtle.bye()

            #Reset turtle graphics environment before restarting
            importlib.reload(turtle)

            main()

        def exit_game():
            """
            Exits the game without restarting.
            """
            global should_restart
            should_restart = False
            popup.destroy()
            turtle.bye()

        play_again_button = tk.Button(popup, text="Play Again", width=12, command=play_again)
        exit_button = tk.Button(popup, text="Exit", width=12, command=exit_game)

        play_again_button.pack(pady=5)
        exit_button.pack(pady=5)

        popup.mainloop()


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
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]) and self.grid[y][x] != '#' # Checks if (x, y) is within grid bounds and not a wall.


    def get_start(self):
        """
        Returns the starting position of the maze.

        Returns: tuple[int, int]: The (x, y) coordinates of the starting position.
        """
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return x, y
        return None


    def get_goal(self):
        """
        Returns the goal position of the maze.

        Returns: tuple[int, int]: The (x, y) coordinates of the goal position.
        """
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'G':
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
        turtle.tracer(0, 0)  # Disable animation
        turtle.speed(0)
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
        turtle.update()


    def update_position(self, x, y):
        """
        Moves the navigator to a new position in the maze.
        :param x: new x-coordinate in the maze grid.
        :param y: new y-coordinate in the maze grid.
        :return:
        """
        cell_size = 20
        start_x = -len(self.maze.grid[0]) * cell_size // 2
        start_y = len(self.maze.grid) * cell_size // 2
        screen_x = start_x + self.x * cell_size + cell_size // 2
        screen_y = start_y - self.y * cell_size - cell_size // 2

        self.turtle.goto(screen_x, screen_y)  # Move turtle using goto (#49)


class MazeGUI:
    def __init__(self):
        """
        Initializes the GUI window, timer, and related components for maze interaction.
        """
        self.window = None      #will be initialized in select_difficulty
        self.difficulty = None  #selected difficulty level
        self.timer = None       #timer label
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

    def show_instructions_window(self):
        instructions_window = tk.Tk()
        instructions_window.title("How to Play")
        instructions_window.geometry("550x550")
        instructions_window.resizable(False, False)
        instructions_window.configure(bg="#f0f8ff")

        title_label = tk.Label(
            instructions_window,
            text="📋 How to Play",
            font=("Arial", 18, "bold"),
            bg="#f0f8ff",
            fg="#003366"
        )
        title_label.pack(pady=15)

        instructions_text = (
            "🎯 Goal:\n"
            "        Help the turtle reach the red square (the goal) as fast as possible!\n\n"
            "🟩 Starting Point:\n"
            "        The turtle starts at the green square.\n\n"
            "🎮 Controls (Arrow Keys):\n"
            "        ⬆️  Up Arrow       = Move up\n"
            "        ⬇️  Down Arrow     = Move down\n"
            "        ⬅️  Left Arrow     = Turn left\n"
            "        ➡️  Right Arrow    = Turn right\n\n"
            "🚫 Rules:\n"
            "        You cannot go through walls (black squares).\n\n"
            "⏱️ Timer:\n"
            "        The timer starts automatically when you move.\n\n"
            "🎉 Winning:\n"
            "        When you reach the goal, your time will be displayed."
        )

        text_label = tk.Label(
            instructions_window,
            text=instructions_text,
            font=("Arial", 12),
            justify="left",
            anchor="w",
            bg="#f0f8ff",
            fg="#003366"
        )
        text_label.pack(pady=10, padx=30, anchor="w")

        ok_button = tk.Button(
            instructions_window,
            text="Got it! Let's Play!",
            width=20,
            command=instructions_window.destroy,
            bg="#4682b4",
            fg="white",
            activebackground="#5f9ea0",
            activeforeground="white"
        )
        ok_button.pack(pady=20)

        instructions_window.mainloop()

    def show_maximize_tip(self):
        """
        Shows a popup message recommending the player to maximize the window for the best game experience.
        """
        tip_window = tk.Tk()
        tip_window.title("Tip for Best Experience")
        tip_window.geometry("400x150")
        tip_window.resizable(False, False)

        tip_label = tk.Label(
            tip_window,
            text="📢 For the best game experience,\nplease maximize your Turtle window before playing!",
            font=("Arial", 12),
            justify="center"
        )
        tip_label.pack(pady=20)

        ok_button = tk.Button(tip_window, text="OK", width=15, command=tip_window.destroy)
        ok_button.pack(pady=10)

        tip_window.mainloop()


    def run(self):
        """
        Runs the Tkinter mainloop to display and maintain the GUI.
        """
        self.maze = Maze()
        self.maze.generate_maze(self.difficulty)

        drawer = MazeDrawer(self.maze)
        drawer.draw_maze()

        start_x, start_y = self.maze.get_start()
        self.navigator = Navigator(self.maze, x=start_x, y=start_y)
        self.navigator.go_to_start()
        self.navigator.bind_keys()

        turtle.done()


def main():
    global should_restart
    should_restart = True  # Reset it each time main() is called

    gui = MazeGUI()
    gui.show_welcome_window()
    gui.show_instructions_window()
    gui.show_maximize_tip()
    gui.select_difficulty()

    if should_restart:
        gui.run()


if __name__ == "__main__":
    main()