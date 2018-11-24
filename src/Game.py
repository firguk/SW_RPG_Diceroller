from src.Dices.Generic.Numeric import Numeric
from src.DicePool import DicePool
from src.Dices.StarWarsRPG.Ability import Ability
from src.Dices.StarWarsRPG.Boost import Boost
from src.Dices.StarWarsRPG.Challenge import Challenge
from src.Dices.StarWarsRPG.Difficulty import Difficulty
from src.Dices.StarWarsRPG.Force import Force
from src.Dices.StarWarsRPG.Proficiency import Proficiency
from src.Dices.StarWarsRPG.Setback import Setback
from src.Lobby import Lobby
from src.Users.GameMaster import GameMaster
from src.Users.Player import Player

if __name__ == "__main__":

    gm = GameMaster("A")
    player1 = Player("C")

    lobby = Lobby(gm)
    lobby.add_player(player1)
    lobby.show_players()

    turn = 0
    while turn < 2:

        print("----------\n%s's turn" % (lobby.get_current_player().get_name()))
        lobby.get_current_player().add_dice(Numeric(6))
        lobby.get_current_player().add_dice(Numeric(20))
        lobby.get_current_player().add_dice(Ability())
        lobby.get_current_player().add_dice(Difficulty())
        lobby.get_current_player().add_dice(Proficiency())
        lobby.get_current_player().add_dice(Challenge())
        lobby.get_current_player().add_dice(Boost())
        lobby.get_current_player().add_dice(Setback())
        lobby.get_current_player().add_dice(Force())

        print("%s throw:\n\t%s" % (lobby.get_current_player().get_name(), lobby.get_current_player().throw()))

        lobby.next_turn()
        turn += 1


