from src.Users.User import User


class Player(User):
    """
    A basic player
    """

    def __init__(self, name):
        super().__init__(name)

    def set_dice_pool(self, dice_pool):
        super().set_dice_pool(dice_pool)

    def add_dice(self, dice):
        super().add_dice(dice)

    def get_name(self):
        return super().get_name()

    def throw(self):
        return super().throw()
