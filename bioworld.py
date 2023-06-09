from random import randint
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
                    3   Credits
                    4   Quit
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
    "credits": r"""
  ____ ____  _____ ____ ___ _____ ____
 / ___|  _ \| ____|  _ \_ _|_   _/ ___|
| |   | |_) |  _| | | | | |  | | \___ \
| |___|  _ <| |___| |_| | |  | |  ___) |
 \____|_| \_\_____|____/___| |_| |____/

This game was made by me, Jacobus Burger from May 26 to
May 28 in 2023 as part of the ASCII Game Jam 2023!

I made the ASCII art by hand, though it's not much to
look at.

I wanted to thank the hosts of this game jam for the fun! And
I wanted to give a special thanks to you for playing my
first ASCII game!

It may not be much, but better games may yet come! Life is growth!

I really hope you enjoy this game, as basic as it is!

Thank you.
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
.     | |  (o)   .
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

DEFEAT THE THREE MACHINE LORDS ABOVE!

    """,
    "win": r"""
  ____ ___  _   _  ____ ____      _  _____ ____  _
 / ___/ _ \| \ | |/ ___|  _ \    / \|_   _/ ___|| |
| |  | | | |  \| | |  _| |_) |  / _ \ | | \___ \| |
| |__| |_| | |\  | |_| |  _ <  / ___ \| |  ___) |_|
 \____\___/|_| \_|\____|_| \_\/_/   \_\_| |____/(_)

You defeated all 3 machine lords, fusing biology and
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
    "faust": r"""
  ___
 /    \
|   |  \
\  -+-  \
 \  |    \
  \       \
   \  v v  \
    \  =   /
     \____/

A machine made for 'medicine' that doesn't know life.
    """,
    "amadeus": r"""
  ____________________________________________
||____|\______________________________________
||____|/__1___________________________________
||___/|___0___________________________________
||__(_|)______________________________________
     '|

A machine made for 'music' that doesn't know song.
    """,
    "picaso": r"""

KRUGKIDHN5QWYIDPMYQGY2LGMUQGS4ZAOJQXA5D
VOJSS4ICBOJ2CA2LTEB2GQZJAO5QXSIDXMUQGK6
DQMVZGSZLOMNSSA2LUFYQEC4TUEBUXGIDUNBSSA
5DSMFXHGZTPOJWWS3THEBSXQ4DFOJUWK3TDMUQC
4LROEBUW45DVNF2GS33OOMWCA53JNRWCYIDXNF2
GQ33VOQQGC4TUFQQGEZJANBUWIZDFNYQGM4TPNU
QHK4ZAMFXGIIDXMUQHO2LMNQQGEZJANRSWM5BAO
5UXI2BANZXXI2DJNZTSAYTVOQQGCIHCQCMHIZLS
NVUW433MN5TXSIDGN5ZCA4DSMFRXI2LDMFWCAZL
OMRZ6FAEZEB3WQ2LDNAQHOZJAMZQWY43FNR4SAY

3BNRWCA3DJMZSS4CQ=

A machine made for 'art' that doesn't know beauty.
    """,
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def read(prompt=''):
    while True:
        choice = input(prompt)
        if not choice.isdigit():
            continue
        else:
            return int(choice)


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


def bioworld():
    # beginning gamestate
    enemies = [(70, 90, "picaso"), (50, 70, "amadeus"), (30, 50, "faust")]
    state = {
        "player": Player(13, 5),
        "enemy": Enemy(*enemies.pop()),
        "biomachines": 0,
    }
    running = False
    
    # stay in menu mode until game starts
    while not running:
        # render menu
        print(ART["menu"])
        choice = read()
        clear()
            # if new game, start a new game
        if choice == 1:
            running = True
            continue
            # if help, show help info
        if choice == 2:
            print(ART["help"])
            input()
            clear()
            # if credits, show credits
        if choice == 3:
            print(ART["credits"])
            input()
            clear()
            # if quit, clear screen and terminate program
        if choice == 4:
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
        choice = read("""
        1 - attack   (10 biomass)
        2 - defend   (5  biomass)
        3 - biospore (30 biomass)
        """)

        # perform action based on user input
        # regenerate machina and biomass
        hp = randint(5, 13)
        bm = randint(7, 13)
        state["player"].bm += bm
        state["player"].hp += hp
        print("Your bm increased by {} and your hp by {}".format(bm, hp))
        state["enemy"].ma += 10
        # player turn
        if choice == 1:
            if state["player"].bm >= 10:
                strike = randint(10, 25)
                print("You struck {} for {} hp".format(state["enemy"].name, strike))
                state["enemy"].hp -= strike
                state["player"].bm -= 10
        if choice == 3:
            if state["player"].bm >= 30 and state["enemy"].hp <= 15:
                print("{} has been weakened, you transform them with biomass!".format(state["enemy"].name))
                state["player"].bm -= 30
                state["enemy"].hp = 0
            else:
                print("Enemy HP was too high, transformation failed!!")
        # machine turn
        hit = randint(3, state["enemy"].ma // 2)
        if choice == 2:
            if state["player"].bm >= 5:
                state["player"].bm -= 5
                hit = randint(0, state["enemy"].ma // 4)
        print("{} attacks you, you lose {} hp".format(state["enemy"].name, hit))
        state["player"].hp -= hit
        state["enemy"].ma -= 15
        if state["enemy"].hp <= 0:
            state["biomachines"] += 1
            print("You've overcome and transformed {}!!".format(state["enemy"].name))
            if len(enemies) > 0:
                print("You've grown and become stronger!")
                state["enemy"] = Enemy(*enemies.pop())
                state["player"] = Player(state["player"].hp * 2, state["player"].bm * 2)
        input()

        # clear screen for new render
        clear()

        # win condition: turn the 3 machine lords into biomachine hybrids
        if state["biomachines"] == 3:
            win(True)
        # lose condition: lose the life within you (health <= 0)
        if state["player"].hp <= 0:
            win(False)



if __name__ == '__main__':
    bioworld()
