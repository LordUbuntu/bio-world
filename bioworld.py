# NOTE: screen must be at least 56 char wide and 12 char tall, run by this assumption
# TODO:
# - find a way to store game data
# - implement gameplay
# - implement ascii art
# - add a dict to store and access art
# - add functions representing abilities, maybe store in dict too
# - make enemy class
import os


ART = {
    "menu": r"""
     ____ ___ _____        _____  ____  _     ____
    | __ )_ _/ _ \ \      / / _ \|  _ \| |   |  _ \
    |  _ \| | | | \ \ /\ / / | | | |_) | |   | | | |
    | |_) | | |_| |\ V  V /| |_| |  _ <| |___| |_| |
    |____/___\___/  \_/\_/  \___/|_| \_\_____|____/

               ==========================
                    1   New Game
                    2   Load Game
                    3   Quit
               ==========================
                            .
    """,
    "enemy": """
    \\\\\\       ///

      --     --
     >%%<   >%%<
      --     --

      >=======<
    """
}


# NOTE: screen must be cleared after each input
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_menu():
    print(ART["menu"])


def render_game(state):
    # render player stats
    print('=' * 25)
    print("player stats")
    # render game art
    print('=' * 25)
    print(ART["enemy"])
    # render enemy stats (if applicable)
    print("enemy stats")
    print('=' * 25)


def bioworld():
    render_menu()
    input()
    clear()
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
    input()  # placeholder for now
                    # perform action based on user input
    clear()
    # win condition: turn the 7 machine lords into bio-machine hybrids
    # lose condition: lose the bio-virus/entity within you (health <= 0)



if __name__ == '__main__':
    bioworld()
