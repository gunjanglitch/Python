# Exercise-01 | Write a program that asks the user for a number then prints the following sentence that number of times: ‘I am back to check on my skills!’ If the number is greater than 10, print this sentence instead: ‘Python conditions and loops are a piece of cake.’ Assume you can only pass positive integers.

number = int(input('Please enter a number: '))
if number > 10:
    print('Python condition and loops are a piece of cake.')
else:
    for i in range(number):
        print('I am back to check on my skills!')


# Exercise-02 | Below is a string, text. It contains a long string of characters. Your task is to iterate over the characters of the string, count uppercase letters and lowercase letters, and print the result:

text = 'ABgvddVICJSdkeprsmgn UTPDvndhtuwPOTNRSjfisuRNSUesajdsa'

lowercase_count = 0
uppercase_count  = 0

for letter in text:
    if letter.islower():
        lowercase_count += 1 
    elif letter.isupper():
        uppercase_count += 1 

print('lowercase: ', lowercase_count)
print('UPPERCASE: ', uppercase_count)


# Exercise-03 | Create a function named is_triangle_possible() that accepts three positive numbers. It should return True if it is possible to create a triangle from line segments of given lengths and False otherwise. With 3 numbers, it is sometimes, but not always, possible to create a triangle: You cannot create a triangle from a = 13, b = 2, and c = 3, but you can from a = 13, b = 9, and c = 10.

def is_triangle_possible(a, b, c):
    if  a+b>c and c+b>a and c+a>b:
        return True
    else:
        return False
      
print(is_triangle_possible(13,2,3))
print(is_triangle_possible(13,9,10))


# Exercise-04 | Create two functions: print_five_times() and speak(). The function print_five_times() should accept one parameter (called sentence) and print it five times. The function speak(sentence, repeat) should have two parameters: sentence (a string of letters), and repeat (a Boolean with a default value set to False). If the repeat parameter is set to False, the function should just print a sentence once. If the repeat parameter is set to True, the function should call the print_five_times() function.

def print_five_times(sentence):
    for i in range(5):
        print(sentence)
        
def speak(sentence, repeat=False):
    if repeat:
        print_five_times(sentence)
    else:
        print(sentence)
        
speak('Hello world!')
speak('Hello world!', repeat=True)


# Exercise-05 | Write a function called find_greater_than() that takes two parameters: a list of numbers and an integer threshold. The function should create a new list containing all numbers in the input list greater than the given threshold. The order of numbers in the result list should be the same as in the input list.

def find_greater_than(int_list, threshold):
    new_list = []
    for integer in int_list:
        if integer > threshold:
            new_list.append(integer)
    return new_list
    
    
int_list = [-3, 2, 8, 15, 31, 5, 4, 12]
threshold = 5 
greater_than_threshold = find_greater_than(int_list,threshold)
print('Numbers greater than', threshold, 'are', greater_than_threshold)


# Exercise-06 | Write a function called find_censored_words() that accepts a list of strings and a list of special characters as its arguments, and prints all censored words from it one by one in separate lines. A word is considered censored if it has at least one character from the special_chars list. Use the word_list variable to test your function. 

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
word_list = ['se#$et', 'Ver*%&$lo', 'di$#^$nt', 'c*%e', 'is', '#%$#@!@#$%^$#']

def find_censored_words(word_list, special_chars):
    censored_words = [] 
    for word in word_list:
        for character in word:
            if character in special_chars:
                censored_words.append(word)  
                break

    print('The censored words are:', ', '.join(censored_words))

find_censored_words(word_list, special_chars)


# Exercise-07 | Create a function find_short_long_word(words_list). The function should return a tuple of the shortest word in the list and the longest word in the list (in that order). If there are multiple words that qualify as the shortest word, return the first shortest word in the list. And if there are multiple words that qualify as the longest word, return the last longest word in the list.

words = ['go', 'run', 'play', 'see', 'my', 'stay']
def find_short_long_word(words_list):
    short_word = words_list[0]
    long_word = words_list[0]
    for word in words_list:
        if len(word) < len(short_word):
            short_word = word 
        elif len(word) >= len(long_word):
            long_word = word
    return(short_word, long_word)
    
wording = find_short_long_word(words)
print('The shortest and longest word in the list is', wording)


# Exercise-08 | we've prepared the test_results variable for you. Your task is to iterate over the values of the dictionary and print all names of people who received less than 45 points.

test_results = {'Jenny': 50, 'Mathew': 45, 'Joe': 30, 'Peter': 40, 'Agness': 50, 'Samantha': 45, 'John': 20}

for key, value in test_results.items():
    if value < 45:
        print(key)


# Exercise-09 | 
