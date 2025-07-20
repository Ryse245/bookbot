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

def sort_on(dict):
    return dict["count"]

def get_sorted_data(book_dictionary):
    #convert dictionary to list of dictionary pairs
    letter_list = []
    for character in book_dictionary:
        if character.isalpha():
            letter_list.append({"character":character,"count":book_dictionary[character]})
    
    #sort list using sort_on
    letter_list.sort(reverse=True, key=sort_on)

    return letter_list