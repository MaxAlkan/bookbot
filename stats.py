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