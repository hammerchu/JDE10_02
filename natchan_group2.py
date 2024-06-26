import random
import string

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
     # Task 1 - count the total number of words in the paragraph that contains vowel characters
    def count_vowel_words(paragraph):
        vowels = set('aeiouAEIOU')
        words = paragraph.split()
        count = sum(1 for word in words if any(char in vowels for char in word))
        return count

    # Task 2 - encode the paragraph by shifting the position of each character by a variable value
    def encode_paragraph(paragraph, shift):
        encoded_chars = []
        for char in paragraph:
            if char in string.ascii_letters:
                shifted = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
                if char.isupper():
                    shifted = shifted.upper()
                encoded_chars.append(shifted)
            else:
                encoded_chars.append(char)
        return ''.join(encoded_chars)

    # Task 3 - Reverse the entire paragraph line by line
    def reverse_lines(paragraph):
        lines = paragraph.split('\n')
        reversed_lines = [line[::-1] for line in lines]
        return '\n'.join(reversed_lines)

    # Task 4 - Reverse the order of characters of each word
    def reverse_word_characters(paragraph):
        words = paragraph.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)

    # Output results for each task
    print("Task 1: Count of words with vowels:", count_vowel_words(paragraph))
    print("Task 2: Encoded paragraph (shift=1):", encode_paragraph(paragraph, 1))
    print("Task 3: Reversed lines:", reverse_lines(paragraph))
    print("Task 4: Reversed word characters:", reverse_word_characters(paragraph))

  
def memberFour():
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
