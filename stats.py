def word_counter(text):
    text_as_list = text.split()
    print(f"Found {len(text_as_list)} total words")
    
def count_character(text):
    result = {}
    for ch in text:
        if ch.lower() in result:
            result[ch.lower()] += 1
        else:
            result[ch.lower()] = 1
    return result
    
def print_report(character_amount):
    sorted_chars = {k:v for k,v in sorted(character_amount.items(), key = lambda x: x[1], reverse = True)}
    for k,v in sorted_chars.items():
        if k.isalpha():
            print(f"{k}: {sorted_chars[k]}")

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list