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
