def count_substring(heystack, needle):
    num = 0
    for i in range(0, len(heystack), len(needle)):
        if needle in heystack:
            num += 1
    
    print(num)

heystack = "babababa"
needle = "baba"
count_substring(heystack, needle)
