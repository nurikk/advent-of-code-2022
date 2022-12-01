def main(input_data: list[str]):
    all_values = []
    current_value = 0
    for calorie in input_data:
        if calorie == "":
            all_values.append(current_value)
            current_value = 0
        else:
            current_value += int(calorie)
    top_3 = list(sorted(all_values))[-3:]
    print(sum(top_3))


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
