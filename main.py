
import sys
from stats import count_words, count_characters, get_char_list, sorted_list, get_sorted_alpha_char_list



def get_books_text(path):
    with open(path) as f:
        return f.read()
    
    
def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_books_text(book_path)
    num_words = count_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print (f"{num_words} words found in the document")
    print("--------- Character Count -------")


    character_dictionary = count_characters(text) 
    data_list = get_sorted_alpha_char_list(character_dictionary)

    for i in data_list:
        key = i["char"]
        value = i["num"]
        print(f"{key} : {value}")
        
 
if __name__ == "__main__":   
    main ()