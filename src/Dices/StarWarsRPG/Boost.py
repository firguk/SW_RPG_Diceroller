import random

from src.Dices.Dice import Dice


class Boost(Dice):
    """
    A dice to throw
    """

    def __init__(self):
        self.__nb_side = 6
        self.__sides = [
            {"advantage": 0, "success": 0},
            {"advantage": 1, "success": 1},
            {"advantage": 0, "success": 0},
            {"advantage": 2, "success": 0},
            {"advantage": 0, "success": 1},
            {"advantage": 1, "success": 0}
        ]
        self.__result = {}

    def __str__(self):
        if self.__result is None:
            return "The dice has not be thrown"
        return "Boost dice\tresult=" + "\n" + \
               "\t\tadvantage:" + str(self.__result["advantage"]) + "\n" + \
               "\t\tsuccess:" + str(self.__result["success"])

    def get_result(self):
        return "ability", self.__result

    """
    throw the dice
    """
    def throw(self):
        self.__result = self.__sides[random.randint(0, self.__nb_side - 1)]
