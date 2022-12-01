def main(input_data: list[str]):
    grand_max = 0
    current_value = 0
    for calorie in input_data:
        if calorie == "":
            if current_value > grand_max:
                grand_max = current_value
            current_value = 0
        else:
            current_value += int(calorie)

    print(grand_max)


if __name__ == "__main__":
    with open('./input.txt') as f:
        main(f.read().splitlines())
