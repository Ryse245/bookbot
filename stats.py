def get_num_words(book_text):
    word_array = book_text.split()
    return len(word_array)

def get_book_data(book_text):
    book_data = {}
    book_text_lower = book_text.lower()
    for character in book_text_lower:
        if character not in book_data:
            book_data[character] = 1
        else:
            book_data[character] += 1

    return book_data