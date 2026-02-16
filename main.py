#Importing modules needed throughout the function
import sys
from stats import get_word_num, char_count, get_report
#Storing added argument as a variable, instructing user to give filepath if non-existent
if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#The purpose of this function is to obtain text from a book file.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
#Main function to generate report
def main():
    book_text = get_book_text(filepath)
    num_words = get_word_num(book_text)
    character_count = char_count(book_text)
    sorted_chars = get_report(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()