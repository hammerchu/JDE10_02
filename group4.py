import random

text = 'C:/Users/KK Chan/Desktop/JDE10/JDE10_02/news.txt'
f = open(text, "r" , encoding="utf-8")
news_text = f.read()
print(news_text)

def hammer_task_0():
    '''example function'''

    teamJDE = ['KKCHAN', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


def memberOne(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for word in text.split():
        for char in word:
            if char.lower() in vowels:
                count += 1
    return count


def memberTwo(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char) + shift
            if char.isupper():
                encoded_text += chr((ascii_val - 65) % 26 + 65)
            else:
                encoded_text += chr((ascii_val - 97) % 26 + 97)
        else:
            encoded_text += char
    return encoded_text


def memberThree(text):
    reversed_lines = []
    lines = text.split('\n')
    for line in lines:
        reversed_line = ''
        i = 0
        while i < len(line):
            if line[i].isspace() or not line[i].isalpha():
                reversed_line += line[i]
                i += 1
            else:
                start = i
                while i < len(line) and line[i].isalpha():
                    i += 1
                word = line[start:i]
                reversed_line += word[::-1]
        reversed_lines.append(reversed_line)
    reversed_text = '\n'.join(reversed_lines)
    return reversed_text


def memberFour(text):
    reversed_words = []
    words = text.split()
    for word in words:
        reversed_words.append(word[::-1])
    reversed_text = ' '.join(reversed_words)
    return reversed_text


if __name__ == "__main__":
    print(hammer_task_0())  # 呼叫 hammer_task_0() 函數
    count_vowel_words = memberOne(news_text)  # 將文本傳遞給 memberOne 函數
    print('Total number of words with vowel characters:', count_vowel_words)
    print('Encoded text:', memberTwo(news_text, 1))  # 將文本傳遞給 memberTwo 函數
    print('Reversed text (line by line):', memberThree(news_text))  # 將文本傳遞給 memberThree 函數
    print('Reversed text (word by word):', memberFour(news_text))  # 將文本傳遞給 memberFour 函數


    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy. -> yob a ma. I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
