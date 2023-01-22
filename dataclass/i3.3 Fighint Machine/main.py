from dataclasses import dataclass
import random


def input_pokemon_type() -> str:
    running = True
    while running:
        player_type = input("Please choose from a type listed above: ")
        if is_valid_type(player_type):
            running = False
            return player_type


def is_valid_type(player_type: str) -> bool:
    if (
        player_type == "Fire"
        or player_type == "Grass"
        or player_type == "Rock"
        or player_type == "Ice"
        or player_type == "Ground"
    ):
        return True
    else:
        print("\033[1m", "Please choose a valid type!", "\033[0m")
        print()
        return False


def random_pokemon_type() -> str:
    enemy_type_number = random.randint(0, 4)
    if enemy_type_number == 0:
        return "Fire"
    elif enemy_type_number == 1:
        return "Grass"
    elif enemy_type_number == 2:
        return "Rock"
    elif enemy_type_number == 3:
        return "Ice"
    elif enemy_type_number == 4:
        return "Ground"


def has_advantage(player_type: str, enemy_type: str) -> bool:
    if player_type == enemy_type:
        return f"You both chose {player_type}! It's a tie!\n"
    else:
        has_fire_advantage = player_type == "Fire" and (
            enemy_type == "Grass" or enemy_type == "Ice"
        )
        has_grass_advantage = player_type == "Grass" and (
            enemy_type == "Rock" or enemy_type == "Ground"
        )
        has_rock_advantage = player_type == "Rock" and (
            enemy_type == "Fire" or enemy_type == "Ice"
        )
        has_ice_advantage = player_type == "Ice" and (
            enemy_type == "Grass" or enemy_type == "Ground"
        )
        has_ground_advantage = player_type == "Ground" and (
            enemy_type == "Fire" or enemy_type == "Rock"
        )
        has_player_advantage = (
            has_fire_advantage
            or has_grass_advantage
            or has_rock_advantage
            or has_ice_advantage
            or has_ground_advantage
        )
        if has_player_advantage:
            return True
        else:
            return False


### ^^^ Functions you should already have  ^^^
###     I just don't want to include the
###     solutions so that someone can't
###     just look ahead and cheat.
### ------------------------------------------
### vvv New stuff you should have to write vvv


@dataclass
class Game:
    playhp: int
    comphp: int


def print_greeting() -> None:
    print(
        """Here are your choices: 
Fire
Grass
Rock
Ice
Ground"""
    )
    print(
        """Remember:
    Fire beats grass and ice 
    Grass beats rock and ground
    Rock beats fire and ice
    Ice beats grass and ground
    Ground beats fire and rock!"""
    )


def is_game_over(game: Game) -> bool:
    if game.playhp <= 0 or game.comphp <= 0:
        return True
    else:
        return False


def play_round(game: Game) -> None:
    player_type = input_pokemon_type()
    enemy_type = random_pokemon_type()
    has_player_advantage = has_advantage(player_type, enemy_type)
    if has_player_advantage:
        print()
        print(f"The computer chose {enemy_type}! You win!")
        game.comphp -= random.randint(10, 30)
    elif not has_player_advantage:
        print()
        print(f"The computer chose {enemy_type}! You lose!")
        game.playhp -= random.randint(10, 30)
    print()
    print("\033[32m", f"Player health: {game.playhp}", "\033[0m")
    print("\033[31m", f"Computer health: {game.comphp}", "\033[0m")
    print()


def is_player_dead(game: Game) -> bool:
    if game.playhp <= 0:
        return True
    else:
        return False


def is_computer_dead(game: Game) -> bool:
    if game.comphp <= 0:
        return True
    else:
        return False


def main():
    print_greeting()
    game = Game(100, 100)

    while not is_game_over(game):
        play_round(game)

    if is_player_dead(game):
        print("You were defeated by the computer!\n")
    elif is_computer_dead(game):
        print("You defeated the computer!\n")


if __name__ == "__main__":
    main()
