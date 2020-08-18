

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    x = {}
    y = []
    weight_list = list(enumerate(weights, 0))
    for i in weight_list:
        x[i[1]] = i[0]
    for tup in x:
        if tup[1] - limit in x:
            y.append(tup[0])
    print(x)
    return None

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)
