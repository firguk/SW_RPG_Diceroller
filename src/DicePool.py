

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
        self.__total["numeric"] = 0
        self.__total["ability"] = {}
        self.__total["ability"]["advantage"] = 0
        self.__total["ability"]["success"] = 0
        self.__total["difficulty"] = {}
        self.__total["difficulty"]["failure"] = 0
        self.__total["difficulty"]["threat"] = 0
        self.__total["force"] = {}
        self.__total["force"]['light'] = 0
        self.__total["force"]['dark'] = 0
        for dice in self.__dices:
            dice.throw()
            (res_type, res_dict) = dice.get_result()
            if res_type == "numeric":
                self.__total["numeric"] += res_dict
            elif res_type == "ability":
                self.__total["ability"]["advantage"] += res_dict["advantage"]
                self.__total["ability"]["success"] += res_dict["success"]
            elif res_type == "difficulty":
                self.__total["difficulty"]["failure"] += res_dict["failure"]
                self.__total["difficulty"]["threat"] += res_dict["threat"]
            elif res_type == "force":
                self.__total["force"]['light'] += res_dict["light"]
                self.__total["force"]['dark'] += res_dict["dark"]
            else:
                print("Error: Unhandle dice: " + res_type + ": " + res_dict)
