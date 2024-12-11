from process_input import process_input

def get_total_distance():
    list_1, list_2 = process_input()

    list_1.sort()
    list_2.sort()

    total_distance = 0
    for i in range(len(list_1)):
        total_distance += abs(list_1[i] - list_2[i])

    return total_distance

print(get_total_distance())