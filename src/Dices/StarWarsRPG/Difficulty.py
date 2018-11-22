import random

from src.Dices.Dice import Dice


class Difficulty(Dice):
    """
    A dice to throw
    """

    def __init__(self):
        self.__nb_side = 8
        self.__sides = [
            {"failure": 0, "threat": 0},
            {"failure": 2, "threat": 0},
            {"failure": 0, "threat": 1},
            {"failure": 0, "threat": 2},
            {"failure": 1, "threat": 1},
            {"failure": 0, "threat": 1},
            {"failure": 1, "threat": 0},
            {"failure": 0, "threat": 1}
        ]
        self.__result = {}

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return "Difficulty dice\tresult=" + "\n" + \
               "\t\tfailure:" + str(self.__result["failure"]) + "\n" + \
               "\t\tthreat:" + str(self.__result["threat"])

    def get_result(self):
        return "difficulty", self.__result

    """
    throw the dice
    """
    def throw(self):
        self.__result = self.__sides[random.randint(0, self.__nb_side - 1)]