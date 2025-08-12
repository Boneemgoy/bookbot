import sys
from stats import number_of_words, number_of_characters, character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        text_content = f.read()
    return text_content

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = number_of_words(book_text)
    char_counts = character_count(book_text)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    for item in char_counts:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
