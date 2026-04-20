"""
File: StepUp.py
Name: Ray
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.


"""

from karel.stanfordkarel import *


def main():
    pass
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper_99()
    move()
    turn_left()

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



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
