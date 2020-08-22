def has_negatives(a):
    """
    YOUR CODE HERE
    """
    x = {}
    result = []
    for i in a:
        if i > 0:
            x[i] = "true"
    for i in a:
        if i < 0:
            if -i in x:
                result.append(-i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
