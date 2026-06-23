def is_pangram(sentence):
    letters = {char for char in sentence.lower() if char.isalpha()}
    return len(letters) ==26
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
print(is_pangram("the quick brown fox jumps over the lazy dog"))