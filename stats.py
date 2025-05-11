def get_num_words(text):
    """
    This function takes a text string and returns the number of words in it.
    """
    words = text.split()
    num_words = len(words)
    return num_words
    

def count_characters(text):
    """
    This function takes a text string and returns the count of specific characters in it.
    """

    d = {}
    for char in text:
        if char.lower() not in d:
            d[char.lower()] = 1
        
        else:
            d[char.lower()] += 1
    return d

def convert_dict(d):
    """
    This function converts the dictionary to a list of dictionaries.
    """
    new_d = []
    for key, value in d.items():
        new_d.append({"char": key, "num": value})
    return new_d


def sort_on(new_d):
    """
    This function tells the dictionary to sort on the values.
    """
    return new_d["num"]

def print_dict(new_d):
    """
    This function prints the dictionary.
    """
    for i in new_d:
        char = i["char"]
        if char.isalpha():
            print(f'{i["char"]}: {i["num"]}')
    return new_d





  
  
  
  
  
  
  
