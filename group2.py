import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def count_words_with_vowels(text):
    # 將內容拆分為段落
    paragraphs = text.split('\n\n')
    
    # 定義元音字符集
    vowels = set("aeiouAEIOU")
    
    # 統計包含元音字符的段落中的單詞總數
    total_word_count = 0
    
    for paragraph in paragraphs:
        # 檢查段落是否包含元音字符
        if any(char in vowels for char in paragraph):
            # 計算段落中的單詞數
            words = paragraph.split()
            total_word_count += len(words)
    
    return total_word_count
  
def def caesar_cipher(text, shift):
    '''Encode the text by shifting each character by the shift value'''
    encoded_text = []
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            encoded_char = chr(start + (ord(char) - start + shift) % 26)
            encoded_text.append(encoded_char)
        else:
            # Non-alphabetic characters remain unchanged
            encoded_text.append(char)
    
    return ''.join(encoded_text)
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer_task_0)
    print(task_1(hammer_task_0))
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
