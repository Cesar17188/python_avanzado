# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    randon_list = [1, 1, 2, 2, 4]
    print(f'removiendo duplicados con una función: {remove_duplicates(randon_list)}')
    my_set = set(randon_list)
    print(f'removiendo duplicados con sets: {my_set}')

if __name__ == '__main__':
    run()