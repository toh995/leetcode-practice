# flatten the array
# [['1'], ['a'], [2, 3], 4]
# [1, 'a', 2, 3, 4]

def flatten(arr: list, parent: list = []) -> list:
    for element in arr:
        if isinstance(element, list):
            flatten(element, parent)
        else:
            parent.append(element)

    return parent


output = flatten([['1'], ['a'], [2, 3], 4])
print(output)
