# stellagama.py
# A module with various useful functions by Omer Golan-Joel
# v2.3, March 31st, 2018
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# import modules
import random
import string
import os
import unittest
import platform


def yn():
    """
    Simple yes or no prompt filtering invalid results
    """
    query = 1
    while query == 1:
        answer = input("Y/N: ")
        if answer in ["y", "Y"]:
            return "yes"

        if answer in ["n", "N"]:
            return "no"

        else:
            print("Invalid Answer")


def random_choice(list):  # input list
    """
    randomly chooses an element from a list.
    """
    element = list[random.randint(0, len(list) - 1)]
    return element  # output randomly-selected element


def dice(n, sides):
    """
    dice-roller
    """
    die = 0
    roll = 0
    while die < n:
        roll = roll + random.randint(1, sides)
        die += 1
    return roll


def pseudo_hex(num):  # inputs number
    """
    converts numbers to Cepheus Engine "Pseudo-Hex"
    now converted to a list.
    """
    num = int(num)
    code = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    num = code[num]
    return num  # outputs "pseudo-hex" number


def current_dir():
    """
    lists the current directory's contents on Windows or Linux
    """
    if platform.system() == "Windows":
        directory = os.listdir(".\\")
    else:
        directory = os.getcwd()
    return directory


def check_file_exists(check_file):
    """
    checks if a file exists in the directory
    """
    if check_file in os.listdir():
        file_exists = True
    else:
        file_exists = False
    return file_exists


def savefile(extension):  # input extension
    """
    file-saving function
    """
    filename = str(input("Please enter file name to generate: "))
    filecheck = filename + "." + extension  # checks in a file with the same name exists in the 		directory
    save = 1
    if check_file_exists(filecheck):
        print(" ")
        print("File already exists. Overwrite?")
        overwrite = yn()
        if overwrite == "y":
            save = 0
        if overwrite == "n":
            filename = input("Please enter new file name to generate: ")
    filename = filename + "." + extension
    return filename  # outpus File name


def clear_screen():
    """
    clear screen function
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def random_line(filename):  # input file name
    """
    randomly chooses a line from a text file
    """
    with open(filename, "r") as line_list:
        line = random_choice(line_list.readlines())
        line = line.strip()
    return line  # output randomly-chosen line


class Getch:
    """
    Gets a single character from standard input.  Does not echo to the
    screen
    """

    def __init__(self):
        try:
            self.impl = GetchWindows()
        except ImportError:
            self.impl = GetchUnix()

    def __call__(self):
        return self.impl()


class GetchUnix:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def getkeypress():
    """
    reads a single keypress
    """
    if platform.system() == "Windows":
        directory = os.listdir(".\\")
        key = Getch()
        return key().decode()  # outputs keypress

    else:
        key = Getch()
        return key()  # outputs keypress


# testing area
# class testpseudohex(unittest.TestCase):
# 	"""
# 	tests for pseudo_hex
# 	"""
# 	def testhex(self):
# 		code=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", 		"M", "N", "P", "Q", "E", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# 		for i in range (0, 34):
# 			self.assertEqual(pseudo_hex(i), code[i])

# class Testdice(unittest.TestCase):
# """
# test the dice function
# """
# def dicetest(self):
# self.assertEqual(dicetest(1, 6), [1, 6])


# if __name__=='__main__':
# unittest.main()

# getch = _Getch()
# print (getkeypress())
