"""
File: PotholeFilling.py
Name: Ray
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *

def put_beeper_99():
    times= 1
    while times <= 99:
        put_beeper()
        times += 1
def turn_right():
    z=1
    while z<=3:
        turn_left()
        z += 1
def turn_around():
    turn_left()
    turn_left()


def single():
    move()
    turn_right()
    move()
    put_beeper_99()
    turn_around()
    move()
    turn_right()
    move()

def main():
    for i in range(3):
        single()
    """

    """
    pass


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
