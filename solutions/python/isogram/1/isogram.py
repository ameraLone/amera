def is_isogram(string):
    cleaned_string = [char.lower()for char in string if char.isalpha()]
    return len(cleaned_string)==len(set(cleaned_string))
print(is_isogram("lumberjacks"))