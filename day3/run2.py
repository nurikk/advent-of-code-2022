from day3.run1 import get_priority


def main(input_data: list[str]):
    priority_sum = 0
    current_group = []
    for record in input_data:
        current_group.append(record)
        if len(current_group) == 3:
            common_chars = set.intersection(*[set(s) for s in current_group])
            common_char = common_chars.pop()
            priority_sum += get_priority(common_char)
            current_group = []

    print(priority_sum)


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
