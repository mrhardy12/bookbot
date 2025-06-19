def get_book_text(filepath):
    with open(filepath) as f:
        raw_text = f.read()
        return raw_text

def count_words(string):
        word_count = len(get_book_text(string).split())
        return word_count

def main():
    num_words = count_words("books/frankenstein.txt")
    print(f"{num_words} words found in the document")

main()