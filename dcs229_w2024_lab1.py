"""Sources:

 fileTo List -->> https://stackoverflow.com/questions/36706734/reading-words-from-a-file-and-putting-into-list

"""
import re
import string
import numpy as np


def fileToList(filePath) -> "[str]": #https://stackoverflow.com/questions/36706734/reading-words-from-a-file-and-putting-into-list
    word_list = []

    with open(filePath, "r") as f:
        for line in f:
            word_list.extend(line.split())


    return word_list

#def sanitize(word_list: [str]) -> [str]:

    """  for word in word_list:
        for char in word:
            if char not in string.ascii_letters:"""
    
def sanitize(word_list):
    sanitized_words = []

    for word in word_list:
        sanitized_word = ''.join(char.upper() for char in word if char.isalpha())
        sanitized_words.append(sanitized_word)

    return sanitized_words

def remove_non_alphabetic(words_list):
    # Define a regular expression pattern to match only alphabetic characters
    pattern = re.compile('[^a-zA-Z]')

    # Use list comprehension to apply the pattern to each word in the list
    cleaned_words = [pattern.sub('', word) for word in words_list]

    return cleaned_words


def countWords(word_list: [str]) -> ([str],[int]):
    unique_words = []
    word_counts = []
    

    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
            word_counts.append(1)
        else:
            index = unique_words.index(word)
            word_counts[index] += 1

    #for i in range(len(unique_words)):
     #   print(f"{unique_words[i]}: {word_counts[i]}")
            
    result_tuple = (unique_words, word_counts)

    return result_tuple
            


def readWords(filename, use_dict=False) -> ([str],[int]):
    #print(fileToList("wilco.txt"))
    word_list = fileToList(filename)
    word_list = sanitize(word_list)
    #print(word_list)

    #print(countWords(word_list))
    freq_tup = countWords(word_list)
    #print(len(freq_tup[0]) == len(freq_tup[1]))

    #print(freq_tup)


    if use_dict:

        pass

    return freq_tup
    
    



def main():

    
    pass

    #print("Testing readWords(test2.txt):")
    #print(f"    Result:     {readWords('test2.txt')}")
    #print(f"    Expecting:  ([BOB, SAM, ALLIN, ROGER], [3, 2, 2, 1]")

if __name__ == "__main__":
    main()



    