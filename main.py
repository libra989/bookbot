from stats import get_num_words, count_characters, convert_dict, sort_on, print_dict


def get_book_text(book):
    """
    This function takes a book object and returns its text content.
    """
    with open(book) as f:
        text = f.read()
    return text


def main():
    """
    Main function to execute the script.
    """
    import sys
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text =get_book_text(book)    
    num = get_num_words(text)
    count = count_characters(text)
    c1 = convert_dict(count)
    c1.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at sys.argv[1]...")
    print("----------- Word Count ----------")
    print(f'Found {num} total words.')
    print("--------- Character Count -------")
    print_dict(c1)
    print("============= END ===============")
main()