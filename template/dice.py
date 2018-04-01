import random

"""
  usage:
    import dice
    roll = dice.roll(1,6,1,0)
    roll_2d6 = dice.roll(1,6,2,0)

    help(dice.roll)
    help(dice.flux)

  Notes:
    Needs tests.
    Can add shortcuts like dice.roll_2d6 or whatever.
"""


def roll(die_min=1, die_max=6, die_count=1, modifier=0):
    """
    (int, int, int, int) -> int

    roll(die_minimum, die_maximum, die_count, modifier)

    Takes lowest number on the die, highest number, number of dice,
    and any modifiers. Returns an int with the random result.
    
    roll(1, 6, 2, 0)
    A number between 2-12

    roll(1,100, 1, 0)
    A number between 1-100

    my_2d6 = roll(1,6,2,0)
    my_d100 = roll(1,100, 1, 0)

    print("Rolled %d on 2d6 and %d on 1d100!" % (my_2d6, my_d100))
    """

    result = modifier
    for x in range(die_count):
        result += random.randint(die_min, die_max)
    return result


def flux():
    """
    () -> int

    flux()
    Returns an int between -5 and 5, inclusive.

    Flux is used in T5.
    """

    flux = 0
    flux = roll(1, 6, 1, 0) - roll(1, 6, 1, 0)
    return flux
