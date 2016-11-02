test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) in [0, 1]:
        return array

    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        if x == pivot:
            equal.append(x)
        if x > pivot:
            greater.append(x)

    return quicksort(less)+equal+quicksort(greater)

print quicksort(test)
