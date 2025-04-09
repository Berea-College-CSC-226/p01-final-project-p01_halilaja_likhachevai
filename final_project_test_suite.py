from final_project import *
from inspect import getframeinfo, stack

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


if __name__ == "__main__":
    test_suite()