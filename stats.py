def get_num_words(text):
    return len(text.split())

def count_characters(text):
    char_dict = {} 
    for c in text:
        lc = c.lower()
        if(lc in char_dict):
            char_dict[lc] += 1
        else:
            char_dict[lc] = 1
    
    return char_dict

def sort_characters(char_dict):

    def sort_on(dict):
        return dict[1]

    char_list = list(char_dict.items())
    char_list.sort(reverse=True, key=sort_on)

    return char_list