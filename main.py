def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = dict(
        sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    )
    # print(chars_dict)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print_dict(sorted_chars_dict)
    print("--- End report ---")
    # print(chars_dict)


def print_dict(dict: dict) -> None:
    for k, v in dict.items():
        if not k.isalpha():
            continue
        print(f"The {k} character was found {v} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
