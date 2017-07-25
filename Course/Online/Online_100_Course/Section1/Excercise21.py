d = {"a": 1, "b": 2, "c": 3}

print(dict(i for i in d.iteritems() if i < 2))