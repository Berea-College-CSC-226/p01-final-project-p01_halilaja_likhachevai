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
import tine


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
    # Test the distance_from_origin() function
    print("Testing distance_from_origin()")
    p1 = Point(3,4)
    try:
        result = p1.distance_from_origin()
        unittest(math.isclose(result, 5.0))
    except:
        unittest(False)

    # Test the user_set() function (skipping because it requires user input)
    print("Testing user_set() - skipped (requires input)")

    # Test the draw_point() function (basic attribute test)
    print("Testing draw_point()")
    try:
        p1.draw_point()
        unittest(p1.turtle is not None)
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