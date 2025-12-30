def sort_on(items):
    return items["num"]

def get_num_words(book_content):
    num_words = len(book_content.split())
    print(f"Found {num_words} total words")

def get_chars(book_content):
    book_lower = book_content.lower()
    book_list = list(book_lower)
    char_count = {}
    for char in book_list:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    print("--------- Character Count -------")
    del char_count[' ']
    char_count_list = []
    for key, value in char_count.items():
        new_single = {"char": key, "num": value}
        char_count_list.append(new_single)
    char_count_list.sort(reverse=True, key=sort_on)
    for item in char_count_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")