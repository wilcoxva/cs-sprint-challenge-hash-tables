import os


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    x = []
    for i in files:
        x.append(i)
    y = os.path.basename(x)

    # How do I get the last part of the path as a key

    # and value is the path
    # Make array of paths as values
    # Make the queries a key
    print(x)
    # return result


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
