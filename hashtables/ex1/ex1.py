def get_indices_of_item_weights(weights, length, limit):
    
    x = dict()
    y = []
    weight_list = list(enumerate(weights, 0))
    for i in weight_list:
        x[i[1]] = i[0]
    for key in x:
        if limit - key in x:
            y.append(key)
    i = y[0]
    j = y[1]
    print(x[i], x[j])
    return (x[i],x[j])

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)
