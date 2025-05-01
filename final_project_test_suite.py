######################################################################
# Author: Iuliia Likhacheva, Arbjosa Halilaj
# Username: likhachevai, halilaja
#
# Assignment: P01: Final Project
#
# Purpose: A test suite to test the final_project.py code
#
######################################################################
# Acknowledgements:
####################################################################################


from final_project import *
from inspect import getframeinfo, stack
import time


def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    lineum = getframeinfo(stack()[1][0]).lineno
    if did_pass:
        msg = f"Test at line {lineum} ok."
    else:
        msg = f"Test at line {lineum} failed."
    print(msg)

def test_navigator():
    print("\n Running tests for Navigator class...")

    #Dummy Turtle and Screen Classes to Disable GUI
    class DummyTurtle:
        def __init__(self):
            self._heading = 0
        def shape(self, s): pass
        def color(self, c): pass
        def penup(self): pass
        def setheading(self, h): self._heading = h
        def heading(self): return self._heading
        def goto(self, x, y): pass
        def showturtle(self): pass
        def hideturtle(self): pass
        def clear(self): pass
        def write(self, *args, **kwargs): pass

    class DummyScreen:
        def ontimer(self, func, t): pass
        def bye(self): pass
        def _incrementudc(self): pass
        def _update(self): pass

    #mock Navigator to Use Dummy GUI
    class MockNavigator(Navigator):
        def __init__(self, maze, x=0, y=0, direction='N'):
            self.x = x
            self.y = y
            self.direction = direction
            self.maze = maze
            self.timer_start = None
            self.is_timer_running = False
            self.turtle = DummyTurtle()
            self.timer_writer = DummyTurtle()
            self.screen = DummyScreen()
            self.set_heading()
        def update_timer(self): pass
        def update_position(self): pass
        def show_end_popup(self, elapsed): pass

    #setup a simple maze
    grid = [['S', ' '], ['#', 'G']]
    maze = Maze(grid)
    navigator = MockNavigator(maze, x=0, y=0)

    #test initial state
    unittest(navigator.x == 0 and navigator.y == 0)
    unittest(navigator.direction == 'N')

    #test get_time_elapsed()
    t1 = navigator.get_time_elapsed()
    time.sleep(0.1)
    t2 = navigator.get_time_elapsed()
    unittest(t2 >= t1)

    #test at_goal() - should be False at start
    unittest(not navigator.at_goal())

    #move to goal position manually and test
    gx, gy = maze.get_goal()
    navigator.x = gx
    navigator.y = gy
    unittest(navigator.at_goal())

    #test move_forward() logic
    test_maze = Maze([['S', ' '], ['#', 'G']])
    nav = MockNavigator(test_maze, x=0, y=0, direction='E')
    nav.move_forward()
    unittest((nav.x, nav.y) == (1, 0))

    #test invalid move into wall
    nav.direction = 'S'  # facing wall
    prev_x, prev_y = nav.x, nav.y
    nav.move_forward()
    unittest((nav.x, nav.y) == (prev_x, prev_y))

    #test move_up()
    nav = MockNavigator(test_maze, x=1, y=1)
    nav.move_up()
    unittest((nav.x, nav.y) == (1, 0))

    #test move_down()
    nav = MockNavigator(test_maze, x=1, y=0)
    nav.move_down()
    unittest((nav.x, nav.y) == (1, 1))

    #test turn_left()
    nav = MockNavigator(test_maze, x=1, y=0)
    nav.turn_left()
    unittest(nav.direction == 'W')

    #test turn_right()
    nav = MockNavigator(test_maze, x=0, y=0)
    nav.turn_right()
    unittest(nav.direction == 'E')

    #test set_heading()
    nav = MockNavigator(test_maze, x=0, y=0)
    nav.direction = 'S'
    nav.set_heading()
    unittest(nav.turtle.heading() == 270)

    #test go_to_start()
    nav = MockNavigator(test_maze, x=1, y=1)
    nav.go_to_start()
    unittest(nav.turtle is not None)  # dummy object still exists

    #test start_timer()
    nav = MockNavigator(test_maze)
    nav.start_timer()
    time.sleep(0.05)
    unittest(nav.get_time_elapsed() >= 0.05)

    print("Navigator tests complete.")


def test_maze():
    print("\n Running tests for Maze class...")

    #test default maze initialization
    m_default = Maze()
    unittest(m_default.grid == [[0, 1], [1, 0]])
    unittest(m_default.start == (0, 0))
    unittest(m_default.goal == (1, 1))

    #test custom maze with known values
    grid = [['S', ' '], ['#', 'G']]
    m = Maze(grid)
    unittest(m.is_path(0, 0))  # 'S' is valid
    unittest(m.is_path(1, 0))  # space is valid
    unittest(not m.is_path(0, 1))  # wall is not valid
    unittest(not m.is_path(2, 2))  # out-of-bounds

    #test get_start() and get_goal()
    unittest(m.get_start() == (0, 0))
    unittest(m.get_goal() == (1, 1))

    #test get_start() returns None if no 'S'
    m_no_start = Maze([['#', ' '], [' ', 'G']])
    unittest(m_no_start.get_start() is None)

    #test get_goal() returns None if no 'G'
    m_no_goal = Maze([['S', ' '], [' ', '#']])
    unittest(m_no_goal.get_goal() is None)

    #test generate_maze with known difficulty and grid constraints
    m.generate_maze("Easy")
    width = len(m.grid[0])
    height = len(m.grid)
    unittest(width == 10)
    unittest(height == 10)

    #check that start and goal are marked properly
    sx, sy = m.get_start()
    gx, gy = m.get_goal()
    unittest(m.grid[sy][sx] == 'S')
    unittest(m.grid[gy][gx] == 'G')
    unittest(m.difficulty == "Easy")

    #check that paths are carved correctly (some non-wall cells exist)
    path_cells = sum(row.count(' ') for row in m.grid)
    unittest(path_cells > 0)

    print("Maze tests complete.")


def test_maze_drawer():
    print("\n Running tests for MazeDrawer class...")

    #create a simple maze grid
    maze = Maze([['S', ' '], ['#', 'G']])
    drawer = MazeDrawer(maze)

    #test initial state
    unittest(drawer.maze == maze)
    unittest(drawer.cell_size == 20)
    unittest(drawer.turtle is None)

    #we can't test draw_maze() and update_position() directly because they rely on turtle GUI
    print("Skipping draw_maze() and update_position() - require Turtle screen.")

    print("MazeDrawer tests complete.")


def test_maze_gui():
    print("\n Running tests for MazeGUI class...")

    gui = MazeGUI()

    #test default constructor state
    unittest(gui.window is None)
    unittest(gui.difficulty is None)
    unittest(gui.timer is None)
    unittest(gui.navigator is None)
    unittest(gui.maze is None)

    #test set_difficulty sets the correct value (simulate without GUI)
    #we'll override the method to avoid calling Tkinter
    gui.window = type('DummyWindow', (), {'destroy': lambda self: None})()  # Fake .destroy()
    gui.set_difficulty("Medium")
    unittest(gui.difficulty == "Medium")

    #GUI methods (cannot test without a display loop)
    print("Skipping GUI-dependent methods: show_welcome_window, select_difficulty, show_instructions_window, show_maximize_tip, and run")

    print("MazeGUI tests complete.")


def run_all_tests():
    print("\n Starting full test suite. ")
    test_navigator()
    test_maze()
    test_maze_drawer()
    test_maze_gui()
    print("\n All tests completed successfully.")

if __name__ == "__main__":
    run_all_tests()