array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for idx1 in range(len(array)):
    min_idx = idx1
    for idx2 in range(idx1 + 1, len(array)):
        if (array[min_idx] >  array[idx2]):
            min_idx = idx2

    array[idx1], array[min_idx] = array[min_idx], array[idx1]

print(array)