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
import math
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

    #setup a simple maze
    grid = [['S', ' '], ['#', 'G']]
    maze = Maze(grid)
    navigator = Navigator(maze, x=0, y=0) #start at (0, 0) which is S

    #test initial position and direction
    unittest(navigator.x == 0 and navigator.y == 0)
    unittest(navigator.direction == 'N')

    #test get_time_elapsed()
    t1 = navigator.get_time_elapsed()
    time.sleep(0.1)
    t2 = navigator.get_time_elapsed()
    unittest(t2 >= t1)

    #test at_goal() - should be False at start
    unittest(not navigator.at_goal())

    #manually move to goal position and test at_goal()
    gx, gy = maze.get_goal()
    navigator.x = gx
    navigator.y = gy
    unittest(navigator.at_goal())

    #test move_forward() logic without GUI by mocking maze layout
    test_maze = Maze([['S', ' '], ['#', 'G']])
    nav = Navigator(test_maze, x=0, y=0, direction='E')  #facing right, should move to (1, 0)
    nav.move_forward()
    unittest((nav.x, nav.y) == (1, 0))

    #test invalid move (into wall)
    nav.direction = 'S'  #facing down, should hit wall at (1, 1)
    prev_x, prev_y = nav.x, nav.y
    nav.move_forward()
    unittest((nav.x, nav.y) == (prev_x, prev_y))  #shouldn't change

    print("Navigator tests complete.")

def test_maze():
    print("\n Running tests for Maze class...")

    #test basic path check
    m = Maze([['S', ' '], ['#', 'G']])
    unittest(m.is_path(0, 0))  #'S' is valid path
    unittest(m.is_path(1, 0))  #space is valid
    unittest(not m.is_path(0, 1))  #wall is not path
    unittest(not m.is_path(2, 2))  #out of bonds

    #test get start and goal position
    unittest(m.get_start() == (0, 0))
    unittest(m.get_goal() == (1, 1))

    #test generate maze with known size
    m.generate_maze("Easy")
    width = len(m.grid[0])
    height = len(m.grid)
    unittest(width == 10)
    unittest(height == 10)
    unittest(m.grid[m.get_start()[1]][m.get_start()[0]] == 'S')
    unittest(m.grid[m.get_goal()[1]][m.get_goal()[0]] == 'G')

    print("Maze tests complete.")

def test_maze_drawer():
    print("\n Running tests for MazeDrawer class...")

    #create a simple maze grid
    maze = Maze([['S', ' '], ['#', 'G']])
    drawer = MazeDrawer(maze)

    #test object setup
    unittest(drawer.cell_size == 20)
    unittest(drawer.maze == maze)

    #can't test draw_maze() directly because it uses Turtle graphics
    print("Skipping draw_maze() and update_position() - requires Turtle screen.")

    print("MazeDrawer tests complete.")

def test_maze_gui():
    print("\n Running tests for MazeGUI class...")

    gui = MazeGUI()

    #initial state checks
    unittest(gui.window is None)
    unittest(gui.difficulty is None)
    unittest(gui.timer is None)
    unittest(gui.navigator is None)
    unittest(gui.maze is None)

    #GUI methods like show_welcome_window, select_difficulty, and run
    #involve real GUI interaction and we can not test them
    print("Skipping show_welcome_Window(), select_difficulty(), and run() - GUI dependent.")

    print("MazeGUI tests complete.")

def run_all_tests():
    print("\n Starting full test suite. ")
    test_maze()
    test_navigator()
    test_maze_drawer()
    test_maze_gui()
    print("\n All tests completed successfully.")

if __name__ == "__main__":
    run_all_tests()