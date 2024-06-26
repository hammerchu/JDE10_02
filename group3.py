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
    pass


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



#Task 1
text = './news.txt'
f = open(text, "r")
with open(text, "r", encoding="utf-8") as f:
    para = f.read()
p=para

#Task 1:
def count_total_num(p):
    Total_num=0
    vowels = ["a", "e", "i", "o", "u"]
    for i in p.lower():
        if i in vowels:
            Total_num += 1
    return Total_num


print(count_total_num(p))

#Task 2
def encode_paragraph(p, shift_value):
    encoded_text = ""
    for char in p:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - 65 + shift_value) + 65)
            else:
                encoded_char = chr((ord(char) - 97 + shift_value) + 97)
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text

shift_value = 1
print(encode_paragraph(para, shift_value))


#Task 3
def reverse_paragraph(paragraph):

    sentences = paragraph.split('.')

    reversed_sentences = [" ".join(sentence.strip().split()[::-1]) for sentence in sentences]
    
    reversed_paragraph = ". ".join(reversed_sentences) + "."
    
    return reversed_paragraph

print(reverse_paragraph(p))


#Task 4
def reverse_word_chars(paragraph):

    sentences = paragraph.split('.')

    reversed_sentences = []
    for sentence in sentences:
        words = sentence.strip().split()
        reversed_words = [word[::-1] for word in words]
        reversed_sentence = ' '.join(reversed_words)
        reversed_sentences.append(reversed_sentence)

    reversed_paragraph = '. '.join(reversed_sentences) + '.'
    
    return reversed_paragraph

print(reverse_word_chars(p))