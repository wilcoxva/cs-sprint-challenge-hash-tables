from os.path import basename

def finder(files, queries):
    # This was my first implementation:
    # result = {}
    # for f in files:
    #     if basename(f) in queries:
    #         if basename(f) not in result:
    #             result[basename(f)] = [f]
    #         else:
    #             result[basename(f)].append(f)
    # var = result.values()
    # arr = [item for sublist in var for item in sublist]
    # return arr
    queries_dict = {}
    result = []
    for query in queries:
        queries_dict[query] = True
    for f in files:
        if basename(f) in queries_dict:
            result.append(f)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
