import random
import re
text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    pass
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer_task_0())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
def count_words_with_vowels(paragraph):
    vowels = set('aeiou')
    word_count = 0
    words = re.findall(r'bw+b', paragraph)
    for word in words:
        if any(char in vowels for char in word):
            word_count += 1
    return word_count

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz


    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I


    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
def reverse_words_order(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_sentence = ' '.join(reversed_words)  # Join the reversed words back to a sentence
    return reversed_sentence

