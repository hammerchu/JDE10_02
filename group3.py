import random

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
    import re

    def invert_word(word):
        # Check if the first character is uppercase
        is_uppercase = word[0].isupper()
        # Invert the word
        inverted_word = word[::-1]
        # If the original word started with uppercase, turn it into lowercase
        if is_uppercase:
            inverted_word = inverted_word[0].lower() + inverted_word[1:]
        return inverted_word

    def invert_text(text):
        words = re.split(r'(\W+)', text)
        inverted_words = [invert_word(word) if word.isalpha() else word for word in words]
        return ''.join(inverted_words)

    with open('./news.txt', 'r') as f:
        text = f.read()
        inverted_text = invert_text(text)
        print(inverted_text)


if __name__ == "__main__":
    print(hammer_task_0())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
