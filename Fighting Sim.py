# player crafts a champion and battles it against npc's with health, attack, and XP

# prompt player to make champion: name, race, skill class (race and skill class give one bonus)
    # assign health and attack
# battle against a goblin (weak stats)
# give player XP'

# may change it to a story-mode later
# may add skill for each race/class

counter = 0

class Champion: # champion object with stats and base attributes
    def __init__(self, name, race, skillclass, weapon, health, attack, dodge):
        self.name = name
        self.race = race
        self.skillclass = skillclass
        self.weapon = weapon
        self.health = health
        self.attack = attack
        self.dodge = dodge

def create_champion(): # character creation
    player_name, player_race, player_skillclass = (input("Name your champion: ")).upper(), \
                                                  (input("choose a Race; select [human or dwarf]: ")).upper(), \
                                                  (input("choose a Class; select [fighter or rogue]: ")).upper()
    player_weapon, player_health, player_attack, can_dodge = [], 0, 0, False

    # denotes stats based on player input
    if player_race == "HUMAN": # human has less health, but more attack
        player_health = 100
        if player_skillclass == "FIGHTER": # fight more dmg, but can't dodge
            player_weapon = "SWORD"
            player_attack = 100
        elif player_skillclass == "ROGUE": # rogue less dmg, but can dodge
            player_weapon = "DAGGER"
            player_attack = 60
    elif player_race == "DWARF": # dwarf has more health, but less attack
        player_health = 150
        if player_skillclass == "FIGHTER":
            player_weapon = "HAMMER"
            player_attack = 80
        elif player_skillclass == "ROGUE":
            player_weapon = "SICKLE"
            player_attack = 40
    if player_skillclass == "ROGUE":
        can_dodge = True

    # assigns champion to chosen attributes
    player_champion = Champion(player_name, player_race, player_skillclass,
                               player_weapon, player_health, player_attack, can_dodge)
    print(f"\nYou have successfully created your champion."
          f" {player_champion.name} is a "
          f"{player_champion.race} {player_champion.skillclass} "
          f"that wields a {player_champion.weapon}.\n")

    display_stats(player_champion)
    challenge_enemy(player_champion, choose_enemy(Champion))

def display_stats(player_champion): # displays current HP and attack values for champion
    print(f"{player_champion.name}\n"
          f"Health: {str(player_champion.health)}\n"
          f"Attack: {str(player_champion.attack)}")

def choose_enemy(Champion): # enemy objects and stats
    enemy_goblin = Champion("Baghoul the Goblin", "Goblinoid", "FIGHTER", "CLUB", 40, 30, False)
    enemy_spider = Champion("Baghoul's Mount Spider", "Spooder", "ROGUE", "FANGS", 240, 50, True)
    enemy_troll = Champion("Danny Devito", "Troll", "FIGHTER", "MAGNUM DONG", 320, 70, True)
    enemy_list = [enemy_goblin, enemy_spider, enemy_troll]
    return enemy_list

# only works when within create character function... need to figure that out
def challenge_enemy(player_champion, enemy_list): # designates enemy for player to fight, and fights them
    print(f"--------------------\nWelcome to the Test Arena! Here, you will battle enemies and level up.\n"
          f"Would you like to go up against Enemy {counter + 1}, {enemy_list[counter].name}?")
    a = input("(y/n): ")
    if a == "y":
        pass
    else:
        print("Thank you for playing Test Arena, Goodbye.")
        exit()
    print(f"\nFight 1: {player_champion.name} vs. {enemy_list[counter].name}")
    combat(counter, player_champion, enemy_list)

# player fights enemy, deals damage to opponents health, and gains XP if the player survives
def combat(counter, player_champion, enemy_list):
    display_stats(player_champion)
    print("\nBegin Combat:")

    if counter == 0:
        print("Baghoul fails to see you through both of his eyepatches."
                f"\nYou attack him for {player_champion.attack} DMG.")
    enemy_list[counter].health -= player_champion.attack
    if enemy_list[counter].health <= 0:
        if counter == 0:
            print("You kill Baghoul with minimal effort - he didn't even see it coming.")
            counter += 1
            challenge_enemy(player_champion, enemy_list)
    else:
        pass




def test_arena():
    create_champion()
    #challenge_enemy()
    #level_up()

test_arena()

# def fight_opponent():
    # set some form of interaction with player before fighting
    # create interface to show attacks, health decreases, text animation, etc...