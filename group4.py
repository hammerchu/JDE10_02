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
    aeiou = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for word in text.split():
        if any(char.lower() in aeiou for char in word):
            count += 1
    return count
    pass
  
def memberTwo():
    shifted = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted += chr((ord(char) - 65 + shift_value) % 26 + 65)
            else:
                shifted += chr((ord(char) - 97 + shift_value) % 26 + 97)
        else:
            shifted += char
    return shifted
    pass
  
def memberThree():
    return '\n'.join(line[::-1] for line in text.split('\n'))
    pass
  
def memberFour():
    return ' '.join(word[::-1] for word in text.split())
    pass


if __name__ == "__main__":
    print(hammer())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
