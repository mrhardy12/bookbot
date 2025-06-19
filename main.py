import sys

from stats import (
    count_words,
    count_characters,
    chars_dict_to_sorted_dict,
)


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = count_words(book_text)
        characters = count_characters(book_text)
        chars_sorted = chars_dict_to_sorted_dict(characters)
        print_report(book_path, num_words, chars_sorted)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()