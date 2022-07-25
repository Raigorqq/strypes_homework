def is_anagram(fst_word, snd_word):
    if (sorted(fst_word.lower) == sorted(snd_word.lower)):
        print("True")
    else:
        print("False")
fst_word = "Name"
snd_word = "naem"

is_anagram(fst_word, snd_word)
