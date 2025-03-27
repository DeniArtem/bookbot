from stats import word_count, characters, sortlist

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    TEXT = get_book_text(book_path)
    num_words = word_count(TEXT)
    char_count = characters(TEXT) # Dictionary of char = num
    char_sorted = sortlist(char_count) # Sorted list by descending numbers of char = num
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")    
    print("--------- Character Count -------")
    for each in char_sorted:
        if each["char"].isalpha():
            print(f"{each['char']}: {each['count']}")
    print("============= END ===============")
    #print(TEXT)


main()
