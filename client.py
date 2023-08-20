from game import Game
from players import Player
def main():
    """Main Function"""

    player = Player()
    player.set_username_from_user_input()

    game=Game(player=player)
    game.start()



if __name__ == "__main__":
    main()    
    

