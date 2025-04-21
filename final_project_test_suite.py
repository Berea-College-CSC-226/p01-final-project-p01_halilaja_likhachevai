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

def test_suite():
    #test Maze.is_path()
    print("Testing Maze.is_path()")
    maze = Maze([['S', ' '], ['#', 'G']])
    unittest(maze.is_path(0, 0)) #start is a path
    unittest(not maze.is_path(0, 1))  #wall
    unittest(maze.is_path(1, 0))  #path
    unittest(not maze.is_path(2, 2))  #out of bounds

    #test Maze.get_start() and Maze.get_goal()
    print("Testing Maze.get_start() and Maze.get_goal()")
    unittest(maze.get_start() == (0, 0))
    unittest(maze.get_goal() == (1, 1))

    #test Maze.generate_maze()
    print("Testing Maze.generate_maze()")
    try:
        maze.generate_maze("Easy")
        start = maze.get_start()
        goal = maze.get_goal()
        unittest(start is not None and goal is not None)
        unittest(maze.grid[start[1]][start[0]] == 'S')
        unittest(maze.grid[goal[1]][goal[0]] == 'G')
    except:
        unittest(False)

    # Test the move_forward() function
    print("Testing move_forward()")

    # Test the turn_left() function
    print("Testing turn_left()")

    # Test the turn_right() function
    print("Testing turn_right()")

    # Test the at_goal() function
    print("Testing at_goal()")

    # Test the get_time_elapsed() function
    print("Testing get_time_elapsed()")
    nav = Navigator(Maze())
    elapsed1 = nav.get_time_elapsed()
    time.sleep(0.1)
    elapsed2 = nav.get_time_elapsed()
    unittest(elapsed2 >= elapsed1)

    # Test the is_path() function
    print("Testing is_path()")

    # Test the get_start() function
    print("Testing get_start()")

    # Test the get_goal() function
    print("Testing get_goal()")

    # Test the generate_maze() function
    print("Testing generate_maze()")

    # Test the draw_maze() function
    print("Testing draw_maze()")

    # Test the draw_navigator() function
    print("Testing draw_navigator()")

    # Test the update_position() function
    print("Testing update_position()")

    # Test the select_difficulty() function
    print("Testing select_difficulty()")

    # Test the start_timer() function
    print("Testing start_timer()")

    # Test the run() function
    print("Testing run()")


if __name__ == "__main__":
    test_suite()