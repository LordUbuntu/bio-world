# TODO:
# - find a way to store game data
# - implement gameplay
# - implement ascii art
# - add a dict to store and access art
# - add functions representing abilities, maybe store in dict too
# - make enemy class
ART = {
    "enemy": """
    \\\\\\       ///

      --     --
     >%%<   >%%<
      --     --

      >=======<
    """
}


def render_game(state):
    # render player stats
    print('=' * 20)
    print("")
    # render art
    print('=' * 20)
    # render enemy stats
    print("enemy stats")
    # show choices
    print('=' * 20)
    print('=' * 20)


def bioworld():
    # render menu
    # get player choice for menu
        # if quit, clear screen and terminate program
        # if load game
            # load game data from file
            # render game
        # if new game, start a new game
            # while in game
                # render game
                render_game({"health": 10, "power": 5})
                # get user input
                    # perform action based on user input
    # win condition: turn the 7 machine lords into bio-machine hybrids
    # lose condition: lose the bio-virus/entity within you (health <= 0)



if __name__ == '__main__':
    bioworld()
