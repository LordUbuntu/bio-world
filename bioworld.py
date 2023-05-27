# TODO:
# - find a way to store game data
# - implement gameplay
# - implement ascii art
# - make enemy class
# - make player class
import os
from sys import exit


# NOTE: screen must be at least 56 char wide and 12 char tall, run by this assumption
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
    "win": r"""
  ____ ___  _   _  ____ ____      _  _____ ____  _
 / ___/ _ \| \ | |/ ___|  _ \    / \|_   _/ ___|| |
| |  | | | |  \| | |  _| |_) |  / _ \ | | \___ \| |
| |__| |_| | |\  | |_| |  _ <  / ___ \| |  ___) |_|
 \____\___/|_| \_|\____|_| \_\/_/   \_\_| |____/(_)

You defeated all 7 machine lords, fusing biology and
machine into an exciting new chimera!! Now flowers can
bloom from your mechanic limbs in the new LIVING world
you've helped grow out of this once hollow and mechanical
one! You're overcome with joy at what new things LIFE
will bring to this changing and caring world!

Keep growing, bio bot!
    """,
    "lose": r"""
  ___  _   _   _   _  ___  _
 / _ \| | | | | \ | |/ _ \| |
| | | | |_| | |  \| | | | | |
| |_| |  _  | | |\  | |_| |_|
 \___/|_| |_| |_| \_|\___/(_)

The machine lords have won, crushing any hope of a
biomechanical future! Another day, another cog in the
machine, another dispensible bot to be replaced in this
factory world! You did all your could, but now you can
only watch helpelessly as nothing changes and this
hollow world goes on unchanging and uncaring! The crusher
decends upon you as you watch in apathy.

Stay still, poor bot!
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
    print("STATS\nhp {}  biomass {}".format(state["player"].hp, state["player"].bm))
    # render game art
    print('=' * 25)
    print(ART[state["enemy"].name])
    # render enemy stats (if applicable)
    print("ENEMY\nhp {}  machina {}".format(state["enemy"].hp, state["enemy"].ma))
    print('=' * 25)


def end():
    exit("Thanks for playing")


def win(condition):
    if condition:
        exit(ART["win"])
    else:
        exit(ART["lose"])


# NOTE:
# - game consists of just boss battles (no other kind of scene)
# - gameplay consists of fighting enemies until you have defeated (make bio of) 7 machines
def bioworld():
    # begin gamestate
    state = {
        "player": Player(),  # TODO: player class with hp and bm
        "enemy": Enemy(),  # TODO: varied enemy class with hp and ma
        "biomachines": 0,
    }
    running = True
    # render menu
    render_menu()
    choice = int(input())  # get player choice for menu
    clear()
        # if quit, clear screen and terminate program
    if choice == 3:
        clear()
        end()
        # if load game
    if choice == 2:
            # load game state from file
        # TODO: implement read_data(file)
        with open("save.txt", 'r') as file:
            state = read_data(file)
        # if new game, start a new game
    if choice == 1:
            # use default state
        continue
            # while in game
    while running:
                # render game
        render_game(state)
                # get user input
        choice = int(input("""
        1 - attack   (10 biomass)
        2 - defend   (5  biomass)
        3 - biospore (30 biomass)
        """))
                    # perform action based on user input
                    # NOTE: the assumption is that all actions in the game are combat choices
        if choice == 3:
            if state["player"].bm >= 30:
                # merge enemy robot with biomass to make biomachine
                pass
        if choice == 2:
            if state["player"].bm >= 5:
                # defend some amount of enemy attack based on amount of biomass
                pass
        if choice == 1:
            if state["player"]bm >= 10:
                # attack some amount of hp based on amount of biomass
                pass
        # clear screen for next render
        clear()
        # win condition: turn the 7 machine lords into biomachine hybrids
        if state["biomachines"] == 7:
            win(True)
        # lose condition: lose the bio-virus/entity within you (health <= 0)
        if state["player"].hp <= 0:
            win(False)



if __name__ == '__main__':
    bioworld()
