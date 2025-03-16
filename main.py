from stats import get_num_words
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    book_path = "./books/frankenstein.txt"

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    num_chars = count_characters(text)
    sorted_chars = sort_characters(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for el in sorted_chars:
        if(el[0].isalpha()):
            print(f"{el[0]}: {el[1]}")

    print("============= END ===============")

main()
