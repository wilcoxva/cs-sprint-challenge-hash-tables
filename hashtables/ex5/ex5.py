import os


def finder(files, queries):
    
    result = {}
    for f in files:
        if os.path.basename(f) in queries:
            result[os.path.basename(f)] = f
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
