def count_words(arr):
    new_dict = {}
    for i in arr:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    print(new_dict)
arr = ["apple", "banana", "apple", "pie"]
count_words(arr)
