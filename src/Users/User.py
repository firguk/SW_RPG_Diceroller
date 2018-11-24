from src.DicePool import DicePool


class User:
    """
    A generic user
    """

    def __init__(self, name):
        self.__name = name
        self.__dice_pool = DicePool()

    def set_dice_pool(self, dice_pool):
        self.__dice_pool = dice_pool

    def add_dice(self, dice):
        print("%s add a %s dice" % (self.get_name(), dice.get_name()))
        self.__dice_pool.add(dice)

    def get_name(self):
        return self.__name

    def throw(self):
        return self.__dice_pool.throw()
