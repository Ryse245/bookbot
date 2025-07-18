from stats import get_num_words
from stats import get_book_data

def get_book_text(filepath):
    book_text = None
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    book_stats = get_book_data(book_text)
    print(book_stats)

main()