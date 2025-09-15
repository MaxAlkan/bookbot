def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(input_text):
    num_words = len(input_text.split())
    return num_words


def main():
    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
