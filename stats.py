def count_words(string):
    word_count = string.split()
    return len(word_count)

def count_characters(text):
    count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in count:
            count[lowered_char] += 1
        else:
            count[lowered_char] = 1
    return count

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_dict(char_count_dict):
    sorted_chars = []
    for char in char_count_dict:
        sorted_chars.append({"char": char, "num": char_count_dict[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars