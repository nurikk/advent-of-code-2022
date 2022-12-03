def get_priority(code: str) -> int:
    if code.islower():
        reducer = -96
    else:
        reducer = -38

    return ord(code) + reducer


def main(input_data: list[str]):
    priority_sum = 0
    for record in input_data:
        first_part, second_part = record[:len(record) // 2], record[len(record) // 2:]
        first_part = set(first_part)
        second_part = set(second_part)
        common = first_part.intersection(second_part).pop()
        priority_sum += get_priority(common)
    print(priority_sum)


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
