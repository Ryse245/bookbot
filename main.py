import sys
from stats import get_num_words
from stats import get_book_data
from stats import get_sorted_data

def get_book_text(filepath):
    book_text = None
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def print_report(path, word_count, letter_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter in letter_list:
        print(f"{letter["character"]}: {letter["count"]}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)

        book_stats = get_book_data(book_text)
        sorted_list = get_sorted_data(book_stats)

        print_report(book_path, num_words, sorted_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()