class Lobby:
    """
    A class to gather Users
    """

    def __init__(self, gm):
        self.__game_master = gm
        self.__current_player = gm
        self.__player_index = 0
        self.__players = [gm]

    def add_player(self, player):
        # if player.get_name() not in self.__players:  # prevent players from having the same name
        #     self.__players.append(player)
        #     print("Player %s joined the lobby." % (player.get_name()))
        # else:
        #     print("player" + player.get_name() + "already exist")
        self.__players.append(player)

    def get_players(self):
        return self.__players

    def show_players(self):
        print("Players in the lobby:")
        for player in self.__players:
            print("\t- %s" % (player.get_name()))

    def get_current_player(self):
        return self.__current_player

    # def set_current_player(self, player):
    #     self.__current_player = player

    def next_turn(self):
        self.__player_index += 1
        if self.__player_index >= len(self.__players):
            self.__player_index = 0
        self.__current_player = self.__players[self.__player_index]
