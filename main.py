from stats import get_num_words, get_book_text, get_chars_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = dict(
        sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    )
    # print(chars_dict)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_dict(sorted_chars_dict)
    print("============= END ===============")
    # print(chars_dict)


def print_dict(dict: dict) -> None:
    for k, v in dict.items():
        if not k.isalpha():
            continue
        # print(f"The {k} character was found {v} times")
        print(f"{k}: {v}")


main()
