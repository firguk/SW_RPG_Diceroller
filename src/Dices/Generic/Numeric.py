import random

from src.Dices.Dice import Dice


class Numeric(Dice):
    """
    A dice to throw
    """

    def __init__(self, nb_side):
        self.__nb_side = nb_side
        self.__sides = list(range(1, self.__nb_side + 1))
        self.__result = None

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return "d" + str(self.__nb_side) + "\tresult=" + str(self.__result)

    def get_result(self):
        return "numeric", self.__result

    """
    throw the dice
    """
    def throw(self):
        self.__result = self.__sides[random.randint(0, self.__nb_side - 1)]
