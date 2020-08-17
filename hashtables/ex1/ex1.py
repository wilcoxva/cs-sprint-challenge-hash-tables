def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    x = {}
    value_list = []
    weight_list = list(enumerate(weights, 0))
    for i in weight_list:
        x[i[1]] = i[0]
    for i in weight_list:
        value_list.append(i[1])
    for weight in weight_list:
        if limit - weight[0] in value_list:
            y = [, weight[1]]
    print(y)
    return None

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)
