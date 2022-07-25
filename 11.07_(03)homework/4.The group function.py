def max_consecutive(items):
    count = {}
    for i in items:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(max(count.values()))
items = [1, 2, 3, 3, 3, 3, 4, 3, 3]
max_consecutive(items)
