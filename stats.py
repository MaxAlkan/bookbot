def word_count(input_text):
    num_words = len(input_text.split())
    return num_words

def  character_count(input_text):
    character_dict = {}
    for input in input_text:
        if input.lower() in character_dict:
            character_dict[input.lower()] += 1
        else:
            character_dict[input.lower()] = 1        
    return character_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(character_count_dict):
    sorted_list = []
    for ch in character_count_dict:
        sorted_list.append({"char": ch, "num" : character_count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list