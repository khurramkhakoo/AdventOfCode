from collections import Counter

from process_input import process_input

def get_similarity_score():
    list_1, list_2 = process_input()
    list_2_counter = Counter(list_2)

    similarity_score = 0
    for num in list_1:
        similarity_score += num * list_2_counter[num]

    return similarity_score

print(get_similarity_score())