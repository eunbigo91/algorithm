def binary_search(input_array, value):
    i = 0
    for v in range(0,len(input_array)):
        if input_array[i] == value:
            return i
        else:
            i = i +1
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
