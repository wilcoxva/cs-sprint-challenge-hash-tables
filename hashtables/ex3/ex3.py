def intersection(arrays):
    in_all = False
    result = dict()
    for i in arrays[0]:
        for array in arrays:
            if i in array:
                in_all = True
            else:
                in_all = False
        if in_all:
            result[i] = True
    print(result)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
