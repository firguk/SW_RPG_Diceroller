import random

from src.Dices.Dice import Dice


class Setback(Dice):
    """
    A dice to throw
    """

    def __init__(self):
        self.__nb_side = 6
        self.__name = "Difficulty"
        self.__sides = [
            {"failure": 0, "threat": 0},
            {"failure": 1, "threat": 0},
            {"failure": 0, "threat": 0},
            {"failure": 1, "threat": 0},
            {"failure": 0, "threat": 1},
            {"failure": 0, "threat": 1}
        ]
        self.__result = {}

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return self.__name + " dice\tresult=" + "\n" + \
               "\t\tfailure:" + str(self.__result["failure"]) + "\n" + \
               "\t\tthreat:" + str(self.__result["threat"])

    def get_result(self):
        return self.__result

    """
    throw the dice
    """
    def throw(self):
        self.__result = self.__sides[random.randint(0, self.__nb_side - 1)]

    def get_name(self):
        return self.__name
