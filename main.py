def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)

    def count_words():
        words = text.split()
        # print(words)
        # print(len(words))
        chars = dict()
        for word in words:
            for char in word.lower():
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
        # return len(words)
        print(chars)

    # print(count_words())
    count_words()


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
