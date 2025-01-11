import os

def read_contents(path):
    with open(path) as f:
        return f.read()
     
def count_words(book_of_string):
    count = len(book_of_string.split())
    return count

def count_characters(book_of_string):
    text_list = book_of_string.split()
    count = {}
    for text in text_list:
        for c in text.lower():
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
    return count

def analysis_report(book="None", word_count=0, char_count={}):
    alphabetical_order = "abcdefghijklmnopqrstuvwxyz"
    os.system("clear")
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    for c in alphabetical_order:
        if c in char_count:
            print(f"The \'{c}\' character was found {char_count[c]} times")
        else:
            pass
    print("--- End report ---")
    return None

def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_contents(book_path)
    word_count = count_words(book_contents)    
    character_count = count_characters(book_contents)
    
    analysis_report(book_path, word_count, character_count)
    return None

main()