def main():
    book = "books/frankenstein.txt"
    contents = get_contents(book)
    words = count_words(contents)
    chars = count_characters(contents)
    char_list = dict_to_list(chars)

    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    for item in char_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")


def get_contents(path):
    with open(path) as f:
        contents = f.read()
    return contents


def count_words(contents):
    words = contents.split()
    return len(words)


def count_characters(contents):
    characters = {}
    contents = contents.lower()
    for c in contents:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters


def sort_on(dict):
    return dict["num"]


def dict_to_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()