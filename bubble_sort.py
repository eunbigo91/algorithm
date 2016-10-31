my_list = [81, 12, 5, 13, 8, 9, 65]

def bubble(before_sort):
    length = len(before_sort) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if before_sort[i] > before_sort[i+1]:
                sorted = False
                before_sort[i], before_sort[i+1] = before_sort[i+1], before_sort[i]

bubble(my_list)
print my_list
