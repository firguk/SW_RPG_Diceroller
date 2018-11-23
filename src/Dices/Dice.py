import random


class Dice:
    """
    A dice to throw
    """

    def __init__(self):
        self.__result = None
        self.__name = None

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return "result=" + str(self.__result)

    """
    get dice result
    :return (dice_type, dice_results)
    """
    def get_result(self):
        return None, self.__result

    def throw(self):
        return None

    def get_name(self):
        return self.__name
