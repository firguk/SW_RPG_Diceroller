import random

from src.Dices.Dice import Dice


class Force(Dice):
    """
    A dice to throw
    """

    def __init__(self):
        self.__nb_side = 12
        self.__name = "Force"
        self.__type = "Force"
        self.__sides = [
            {"light": 0, "dark": 1},
            {"light": 0, "dark": 1},
            {"light": 0, "dark": 1},
            {"light": 0, "dark": 1},
            {"light": 0, "dark": 1},
            {"light": 0, "dark": 1},
            {"light": 1, "dark": 0},
            {"light": 1, "dark": 0},
            {"light": 2, "dark": 0},
            {"light": 2, "dark": 0},
            {"light": 2, "dark": 0},
            {"light": 0, "dark": 2}
        ]
        self.__result = {}

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return self.__name + " dice\tresult=" + "\n" + \
               "\t\tlight:" + str(self.__result["light"]) + "\n" + \
               "\t\tdark:" + str(self.__result["dark"])

    def get_name(self):
        return self.__name

    def get_result(self):
        return self.__result

    def get_type(self):
        return self.__type

    """
    throw the dice
    """
    def throw(self):
        self.__result = self.__sides[random.randint(0, self.__nb_side - 1)]

