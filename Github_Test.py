1.
pi = 3.14159265359
def circle(redius):
    sphere = (4*pi*redius**3)/3
    return sphere

print(circle(2))

2.
def given_range(num, low, high):
    if num in range(low,high+1):
        return f'{num} is in range'
    else:
        return 'Error'


print(given_range(3,1,10))

3.
def upper(string):
    up = 0
    low = 0
    for letter in string:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1

    return f'There are {up} upper case characters\nThere are {low} lower case characters'
print(upper('Hello Mr.Rogers, how are you this fine Tuesday'))

4.
def unique(mylist):
    unique_item = []
    for item in mylist:
        if item not in unique_item:
            unique_item.append(item)
        else:
            pass
    return unique_item

print(unique([1,1,1,1,2,2,2,3,3,3,4,5,5]))

5.
def multiply(*args):
    x = 1
    for item in args:
        x = x*item
    return x

print(multiply(1,2,3,-4))

6.
def palindrome(string):
    str_string = list(string)
    str_string.reverse()
    backwords = ''.join(str_string)
    if string == backwords:
        return True
    else:
        return False

print(palindrome('kayak'))

7.
def alpha(sentance):
    import string
    alphabet = string.ascii_lowercase
    reorgenized = []
    for letter in sentance:
        if letter in list(alphabet):
            if letter not in reorgenized:
                reorgenized.append(letter)
        else:
            pass
    reorgenized.sort()
    if reorgenized == list(alphabet):
        return True
    else:
        return False

print(alpha('The quick brown fox jumps over the lazy dog'))




def updated_list():             #updated list
    return [' ',' ',' ']

def ball_location(my_list):             #ball location
    index_question = input("What index would you like to pick (0-2) ")
    value_question = input("What is your value? ")
    my_list[int(index_question)] = value_question
    return my_list

my_list = updated_list()

while True:
    print(f'Current list: {my_list}')
    my_list = ball_location(my_list)
    running = input('Would you like to keep going? Yes/No')
    if running == 'Yes':
        break







