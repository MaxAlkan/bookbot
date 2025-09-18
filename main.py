from stats import word_count, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def book_report(input_text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_text}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text(input_text))} total words")
    print("--------- Character Count -------")
    print(character_count(get_book_text(input_text)))
    
def main():
    book_report("./books/frankenstein.txt")

main()
