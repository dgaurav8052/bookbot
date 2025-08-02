def count_words (text):
    words = text.split()
    return len(words)


def count_characters (text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def get_char_list(word_dict):
    emp_list = []
    for word in word_dict:
        emp_dir = {}
        emp_dir["char"] = word
        emp_dir["num"] = word_dict[word]
        emp_list.append(emp_dir)
    return emp_list


def sorted_list (word_dict):
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)



def get_sorted_alpha_char_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

    

