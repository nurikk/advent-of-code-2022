from enum import Enum


class RockScissorsPaper(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


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

    WIN = 6
    DRAW = 3
    winning = {
        RockScissorsPaper.ROCK: RockScissorsPaper.PAPER,
        RockScissorsPaper.SCISSORS: RockScissorsPaper.ROCK,
        RockScissorsPaper.PAPER: RockScissorsPaper.SCISSORS
    }

    score = 0
    for round_params in input_data:
        opponent_choice, my_choice = round_params.split(' ')
        if winning[opponent_map[opponent_choice]] == my_map[my_choice]:
            score += WIN
        elif opponent_map[opponent_choice] == my_map[my_choice]:
            score += DRAW
        score += my_map[my_choice].value
    print(score)


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
