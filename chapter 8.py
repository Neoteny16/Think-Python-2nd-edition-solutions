fruit = 'banana'

# index = 0
# while index < len(fruit):
#     print(index)
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

def backwardstr(s):
    index = -1
    while index >= -len(fruit):
        letter = s[index]
        print(letter)
        index = index - 1

# backwardstr(fruit)

# for letter in fruit:
#     print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

# for letter in prefixes:
#     if letter in "OQ":
#     # if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     print(letter + suffix)


def find(word, letter, start=0):
    '''
    finds index of a letter in a word, if not return -1
    start - an index where it should start searching(optional)
    '''
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(fruit, 'n'))

# count = 0
# for letter in fruit:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(s, letter):
    '''
    counts appereance of letter in s(str)
    '''
    counter = 0
    for char in s:
        if char == letter:
            counter = counter + 1
    return counter

def count(s, letter):
    '''
    counts appereance of letter in s(str)
    '''
    counter = 0
    for char in s:
        if char == letter:
            counter = counter + 1
    return counter


print(count(fruit, 'a'))

ball = 'ananas'

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


in_both(fruit, ball)

def is_reverse(word1, word2):
    '''
    checks if two words are reverse themselves
    '''
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1 # first error: index out of range, cuz len(word)
    
    while j >= 0:   # second error: not performing last iteration because condition was j>0
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True

print(is_reverse('otar', 'rato'))