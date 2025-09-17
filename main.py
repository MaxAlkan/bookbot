from stats import word_count, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

    char_count = character_count(get_book_text("./books/frankenstein.txt"))
    print(char_count)

main()
