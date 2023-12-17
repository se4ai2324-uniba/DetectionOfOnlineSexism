"""
Module: test_overfit
Description: This code snippet verifies if the Python version matches
the project's requirements, raising an error if not, and confirming
compatibility if the versions align.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""

#pylint: disable=consider-using-f-string
#pylint: disable=no-else-raise

import sys

REQUIRED_PYTHON = "python3"


def main():
    """
    Function: main
    Description: main function
    """
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: f{}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python f{}. Found: Python f{}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
