

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
        self.logic()

    def add_dice_result_to_total(self, dice):
        if not dice.get_type() in self.__total:  # first time we throw this type of dice
            print("Adding %s type dice for %s dice" % (dice.get_type(), dice.get_name()))
            self.add_dice_type_to_total(dice)
        res_dict = dice.get_result()

        for side_name in dice.get_result().keys():
            self.__total[dice.get_type()][side_name] += res_dict[side_name]

    def add_dice_type_to_total(self, dice):
        self.__total[dice.get_type()] = {}
        for side_name in dice.get_result().keys():
            self.__total[dice.get_type()][side_name] = 0

    def logic(self):
        if "Positive" in self.__total:
            if "Negative" in self.__total:
                if self.__total["Positive"]["success"] >= self.__total["Negative"]["failure"]:  # TODO: check rules
                    print("The throw is a success (%d) " %
                          (self.__total["Positive"]["success"] - self.__total["Negative"]["failure"]))
                else:
                    print("The throw is a failure (%d) " %
                          (self.__total["Positive"]["success"] - self.__total["Negative"]["failure"]))
                if self.__total["Positive"]["advantage"] >= self.__total["Negative"]["threat"]:  # TODO: check rules
                    print("with %d advantage" % (self.__total["Positive"]["advantage"] - self.__total["Negative"]["threat"]))
                else:
                    print("with %d threat" % (self.__total["Positive"]["advantage"] - self.__total["Negative"]["threat"]))

