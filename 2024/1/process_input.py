def process_input():
    list_1, list_2 = [], []
    with open("input.txt", "r") as file:
        for line in file:
            item_1, item_2 = line.split("   ")
            list_1.append(int(item_1))
            list_2.append(int(item_2))

    return list_1, list_2