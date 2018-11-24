

class DicePool:
    """
    A pool of dice
    """

    def __init__(self):
        self.__dices = []
        self.__total = {}

    def __str__(self):
        result = ""
        for dice in self.__dices:
            result += str(dice) + "\n"
        result += "========== result ==========" + "\n" + \
                  str(self.__total)
        return result

    """
    add a dice to the dice pool
    :type dice: Dice
    :param dice: the dice to add
    """
    def add(self, dice):
        self.__dices.append(dice)

    """
    remove all dices from dice pool
    """
    def remove_all(self):
        self.__dices = []
        self.__total = {}

    """
    throw all the dices and calculate the total
    """
    def throw(self):
        for dice in self.__dices:
            # print("Throwing %s %s dice" % (dice.get_type(), dice.get_name()))
            dice.throw()
            self.add_dice_result_to_total(dice)
        return self.logic()

    def add_dice_result_to_total(self, dice):
        if not dice.get_type() in self.__total:  # first time we throw this type of dice
            # print("Adding %s type dice for %s dice" % (dice.get_type(), dice.get_name()))
            self.add_dice_type_to_total(dice)
        res_dict = dice.get_result()

        for side_name in dice.get_result().keys():
            self.__total[dice.get_type()][side_name] += res_dict[side_name]

    def add_dice_type_to_total(self, dice):
        self.__total[dice.get_type()] = {}
        for side_name in dice.get_result().keys():
            self.__total[dice.get_type()][side_name] = 0

    """
    subtract dice sides and return a dict containing the result of the subsraction
    :type side_1: dict
    :type side_2: dict
    """
    def subtract_sides(self, side_1, side_2):
        if side_1 in self.__total:
            if side_2 in self.__total:
                if side_1 >= side_2:  # TODO: check rules
                    return side_1 - side_2
                else:
                    return side_2 - side_2

    def logic(self):
        result = {}
        # print(self.__total)
        if "Positive" in self.__total:
            if "Negative" in self.__total:

                # triumph / despair
                if self.__total["Positive"]["triumph"] > self.__total["Negative"]["despair"]:
                    if "Positive" not in result:
                        result["Positive"] = {}
                    result["Positive"]["triumph"] = self.__total["Positive"]["triumph"] - \
                                                    self.__total["Negative"]["despair"]
                if self.__total["Positive"]["triumph"] < self.__total["Negative"]["despair"]:
                    if "Negative" not in result:
                        result["Negative"] = {}
                    result["Negative"]["threat"] = self.__total["Negative"]["despair"] - \
                                                   self.__total["Positive"]["triumph"]

                # success / failure
                if self.__total["Positive"]["success"] > self.__total["Negative"]["failure"]:  # TODO: check rules
                    if "Positive" not in result:
                        result["Positive"] = {}
                    result["Positive"]["success"] = self.__total["Positive"]["success"] - \
                                                    self.__total["Negative"]["failure"]
                if self.__total["Positive"]["success"] < self.__total["Negative"]["failure"]:
                    if "Negative" not in result:
                        result["Negative"] = {}
                    result["Negative"]["failure"] = self.__total["Negative"]["failure"] - \
                                                    self.__total["Positive"]["success"]

                # advantage / threat
                if self.__total["Positive"]["advantage"] > self.__total["Negative"]["threat"]:  # TODO: check rules
                    if "Positive" not in result:
                        result["Positive"] = {}
                    result["Positive"]["advantage"] = self.__total["Positive"]["advantage"] - \
                                                      self.__total["Negative"]["threat"]
                if self.__total["Positive"]["advantage"] < self.__total["Negative"]["threat"]:
                    if "Negative" not in result:
                        result["Negative"] = {}
                    result["Negative"]["threat"] = self.__total["Negative"]["threat"] - \
                                                   self.__total["Positive"]["advantage"]
        return result
