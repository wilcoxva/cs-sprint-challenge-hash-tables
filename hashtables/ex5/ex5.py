from os.path import basename

def finder(files, queries):
    result = {}
    for f in files:
        if basename(f) in queries:
            if basename(f) not in result:
                result[basename(f)] = [f]
            else:
                result[basename(f)].append(f)
    var = result.values()
    arr = [item for sublist in var for item in sublist]
    return arr


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
