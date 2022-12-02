from enum import Enum

from day2.run1 import RockScissorsPaper


def swap_values_and_keys(inp: dict[str, any]) -> dict[str, any]:
    return dict((v, k) for k, v in inp.items())


def main(input_data: list[str]):
    opponent_map = {
        'A': RockScissorsPaper.ROCK,
        'B': RockScissorsPaper.PAPER,
        'C': RockScissorsPaper.SCISSORS
    }
    my_map = {
        'X': RockScissorsPaper.ROCK,
        'Y': RockScissorsPaper.PAPER,
        'Z': RockScissorsPaper.SCISSORS
    }

    my_map_rev = swap_values_and_keys(my_map)
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    outcomes = {
        'X': 'loose',
        'Y': 'draw',
        'Z': 'win'
    }

    WIN = 6
    DRAW = 3
    winning = {
        RockScissorsPaper.ROCK: RockScissorsPaper.PAPER,
        RockScissorsPaper.SCISSORS: RockScissorsPaper.ROCK,
        RockScissorsPaper.PAPER: RockScissorsPaper.SCISSORS
    }
    loosing = swap_values_and_keys(winning)

    score = 0
    for round_params in input_data:
        opponent_choice, target_choice = round_params.split(' ')
        if outcomes[target_choice] == "win":
            my_choice = my_map_rev[winning[opponent_map[opponent_choice]]]
        elif outcomes[target_choice] == "loose":
            my_choice = my_map_rev[loosing[opponent_map[opponent_choice]]]
        else:
            my_choice = my_map_rev[opponent_map[opponent_choice]]

        if winning[opponent_map[opponent_choice]] == my_map[my_choice]:
            score += WIN
        elif opponent_map[opponent_choice] == my_map[my_choice]:
            score += DRAW
        score += my_map[my_choice].value
    print(score)


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
