import random

from src.Dices.Dice import Dice


class Numeric(Dice):
    """
    A dice to throw
    """

    def __init__(self, nb_side):
        self.__nb_side = nb_side
        self.__name = "numeric"  # "d" + str(self.__nb_side)
        self.__sides = list(range(1, self.__nb_side + 1))
        self.__result = None

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return self.__name + "d" + self.__nb_side + "\tresult=" + str(self.__result["numeric"])

    def get_result(self):
        return self.__result

    """
    throw the dice
    """
    def throw(self):
        self.__result = {"numeric": self.__sides[random.randint(0, self.__nb_side - 1)]}

    def get_name(self):
        return self.__name
