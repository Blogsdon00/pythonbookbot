#This function obtains word number given book_text as a string
def get_word_num(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

#This function will count a given character
def char_count(book_text):
    characters = {}
    for character in book_text:
        lowercase_char = character.lower()
        if lowercase_char in characters:
            characters[lowercase_char] += 1
        else: characters[lowercase_char] = 1
    return characters
    
#Sorting helper for report
def sort_on(characters):
    return characters["num"]

def get_report(characters):
    sorted_characters_list = []
    for character in characters:
        sorted_dict = {"char": character, "num": characters[character]}
        sorted_characters_list.append(sorted_dict)
    sorted_characters_list.sort(reverse=True, key=sort_on)
    return sorted_characters_list
