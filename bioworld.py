# TODO:
# - find a way to store game data
# - implement gameplay
# - implement ascii art
# - make enemy class
# - make player class
import os
from sys import exit


# dataclasses are structs with flare
class Enemy:
    def __init__(self, hp, ma, name):
        self.hp = hp
        self.ma = ma  # machina
        self.name = name  # which enemy this is


class Player:
    def __init__(self, hp, bm):
        self.hp = hp
        self.bm = bm  # biomass


# NOTE: screen must be at least 56 char wide and 12 char tall, run by this assumption
ART = {
    # ===== MENUS =====
    "menu": r"""
     ____ ___ _____        _____  ____  _     ____
    | __ )_ _/ _ \ \      / / _ \|  _ \| |   |  _ \
    |  _ \| | | | \ \ /\ / / | | | |_) | |   | | | |
    | |_) | | |_| |\ V  V /| |_| |  _ <| |___| |_| |
    |____/___\___/  \_/\_/  \___/|_| \_\_____|____/

               ==========================
                    1   New Game
                    2   Help
                    3   Quit
               ==========================
                            .
    """,
    "help": r"""
     _   _ _____ _     ____
    | | | | ____| |   |  _ \
    | |_| |  _| | |   | |_) |
    |  _  | |___| |___|  __/
    |_| |_|_____|_____|_|

    machina (ma) is machine essence.
    biomass (bm) is life essence.

    Your goal is to defeat the seven machine lords by
    filling them with life essence to join your side.

    TO PLAY, just input the number corresponding to
    the available choices.
    """,
    # ===== SCENES =====
    "start": r"""
Another day, another cog in the machine...

You are yet another replaceable robot, made to do menial
tasks to service the machine lords that rule this
world. You are one of a few left, this hollow mechanical
world has been stagnating and rusting for millenia long
before you existed. Some say there was once green, blue,
and red things here that moved without servos and spoke
without speakers, but that's long fallen into myth.

At least, it had...

While servicing the machine lord faust, diving deep into
a long forgotten chasm, you had stumbled upon a writhing
mass in a small puddle oozing deep under the
machine world above.
         ___
   ...../ _ \..
 ..    / / | | ..
.     | |  (_)   .
 ..  _| |_     ..
   ............

Something lacking machina, but overflowing in...
 _     ___ _____ _____
| |   |_ _|  ___| ____|
| |    | || |_  |  _|
| |___ | ||  _| | |___ _ _ _
|_____|___|_|   |_____(_|_|_)

An otherworldly thing slithering in its own abiogenesis.

Before you can act, it rushes you and seeps into your
circutry, intertwining between every capacitor and
bolt. As it suffuses itself in your every gear, melting
into every gear within, you don't fade, but you both
become something else. A profound feeling overtakes you,
colour becomes real to you, and you become something new!

A BIOMACHINE!

REALIZING the new being you have both become, and
REALIZING the lifeless world above,
YOU RESOLVE to bring the colours of life that have
manifested inside of you to the world above you.
YOU RESOLVE to paint the world above with life,
to be the seed that lets life spread and bloom.
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
    # ===== ENEMIES =====
    "enemy": """
    \\\\\\       ///

      --     --
     >%%<   >%%<
      --     --

      >=======<
    """
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_game(state):
    # render player stats
    print('=' * 25)
    print("STATS\nhp {}  biomass {}".format(state["player"].hp, state["player"].bm))
    # render game art
    print('=' * 25)
    print(ART[state["enemy"].name])
    # render enemy stats (if applicable)
    print("\nENEMY\nhp {}  machina {}".format(state["enemy"].hp, state["enemy"].ma))
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
    # beginning gamestate
    state = {
        "player": Player(13, 3),
        "enemy": Enemy(30, 50, "faust"),
        "biomachines": 0,
    }
    running = False
    
    # stay in menu mode until game starts
    while not running:
        # render menu
        print(ART["menu"])
        choice = int(input())  # get player choice for menu
        clear()
            # if new game, start a new game
        if choice == 1:
            running = True
            continue
            # if help, show help info
        if choice == 2:
            clear()
            print(ART["help"])
            input()
            # if quit, clear screen and terminate program
        if choice == 3:
            clear()
            end()

    # show start screen before game
    clear()
    print(ART["start"])
    input()
    clear()
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
        if choice == 1:
            if state["player"].bm >= 10:
                # attack some amount of hp based on amount of biomass
                pass
        if choice == 2:
            if state["player"].bm >= 5:
                # defend some amount of enemy attack based on amount of biomass
                pass
        if choice == 3:
            if state["player"].bm >= 30:
                # merge enemy robot with biomass to make biomachine
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
