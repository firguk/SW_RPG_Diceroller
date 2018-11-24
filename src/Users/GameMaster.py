from src.DicePool import DicePool
from src.Users.User import User


class GameMaster(User):
    """
    A GameMaster user
    """

    def __init__(self, name):
        super().__init__(name)

    def set_dice_pool(self, dice_pool):
        super().set_dice_pool(dice_pool)

    def add_dice(self, dice):
        super().add_dice(dice)

    def get_name(self):
        return "(GM) " + super().get_name()

    def throw(self):
        return super().throw()
