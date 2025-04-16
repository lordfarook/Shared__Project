from PyQt5.QtCore.QTimeZone import kwargs
from defer import return_value
from Udemy import capitalize

'Shortcuts'
ctrl + R ---> to replace 'x' to a 'y'
ctrl + / ---> to disable all the lines selected (basically put at all the beggining of the lines '#')

physics, math, english
sum_grades_student.append(grade)    #adds to a list

print("{}".format(""))
name = "or"
print(name.upper())

record = 3.1415926535
r = record
print("your best record is {0:10.5f}".format(record))   /   print(f"your best record is {record:10.5f}")
a = 0.123456789 -----> 0.123      print(f"{a:.3f}")       []

"join command:"
my_list = []
new_my_list = ", ".join(mylist)
x = "".join(y)   -----   join command allows us to take all the items inside y '{may be list, dict.(keys), dict.(values) ....}' and put inside between them whatever I put in ""

"map command"
map(function, intrable)
my_list = ['1','2','3','4','5']
print(sum(map(int, my_list)))  ----- map command allows us to convert a list '(iterable)' to a number/somethingh else '(function)'

"from random import (ctrl + space)" -----> will give us the option for randint, shuffle, and more
from random import randint
random_num = randint(0, 100)   'randit' gives us the option to get a random number between the numbers a to b
print(random_num)
from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   "shuffle" gives us the optoin to shuffle a list, the items inside it
shuffle(my_list)
print(my_list)


.                                        'LIST' []

"append()" command allows you to add the item in () to the end of the list
"pop" command allows you to delete on item from your list
"my_list[-1]" will allow you to replace the item in the place selected "(-1)" to the one you equaled to ("apple")
"sort" command reorgenizes the items in the list to (abcde and 12345)
"reverse" command reverses the items inside the list so the last will be the first and the opposite
"count('a')" command will count how many time 'a' is included in the list
"index('a')" command will show me the first index (place on the list) of 'a'
"my_list.strip()" command eliminates all spaces ('  ') in the list
"my_list.split(",")" command helps if, for example I have a string ---> it will break it to sub-strings
"my_list.capitalize()" command capitalize the first letter in the word (hello -> Hello)

my_list = ["milk", 97, 23.334]
my_list.append(93)
my_list[-1] = "apple"
my_list.pop(-2)
my_list.sort()
my_list.reverse()
my_list.count('a')
my_list.index('a')
my_list.strip()
my_list.split(",")
my_list.capitalize()



.                                     'DICTIONARY' {}

In a dict you can have list, dict, string, float, numbers.
you can also add more dict with the dict['k3']=100
"my_dict.keys()" command shows me all the keys in the dict
"my_dict.values()" command shows me all the values of the keys in the dict
"my_dict.items()" command shows the items -> every "key&value" together ('k3',100)
my_dict = {'k1': 100, 'k2': 'money'}
my_dict.keys()
my_dict.values()
my_dict.items()


.                                       'tuples'  ()

tuples are like lists, the only major change is that the are immuable.
the great benefit of it comes in advanced programing


.                                          'set'

A set is a unique command which if the same item exists twise at in the output we will get it ones, like the example:
myset.add() command allows us to add items to the set

myset = set()
myset.add(1)
myset.add(2)
myset.add(1)
print(myset)
input("{1, 2}")


.                                       'booleans-bool'

True
False

.                                       'opening file'

with open("myfile.txt", "w") as file:
    file.write("""hello this is the firstweekday
this the is the second line
this is the third line
""")



.                                        'For Loops'

for_list = [1,2,3,4]
for x in for_list:
    print('hello')          [option 1]    it will print() 'hello' over and over again by the num of items in the list (here it is 4)

    print(x)                [option 2]    it will print() the value of item inside the list until it will print() all the items

for_list = [1,2,3,4,5,6,7,8,9]
for x in for_list:
    if x % 2 == 0:          (we will get numbers in the list that they are /2 without a remainder '[becuse of %2]') -----> Only even numbers
        print(x)            will get us all the 'even numbers' inside for_list


for_list = [((5,6),78), ('first', 'second'), (1, 2), ('third', 'forth'), (3,4)]
for a,b in for_list:
    print(a)                 it will print(a) the 'first' in every place in the list
                             print(b) will just print the 'second'

"output:"
(5, 6)
first
1
third
3


for_dict = {'k1': 1, 'k2': 2, 'k3': 3}
for x in for_dict:
    print(x)                 will print us only the keys (k1, k2, k3)


for x in for_dict.items():  for_dict'.items()' breaks down the dictionary to keys and values.
    print(x)                now we will get by print(x)   the key and it is attached value together ('k1', 1) ('k2', 2) ('k3', 3)


for key, value in for_dict.items():
    print(key)              will print() the 'first' in every place which are the keys
    print(value)            will print() the 'second' in every place which are the values




break ,     continue ,    pass:

for_list = [1,2,3,4]
for num in for_list:
    #damn
    pass                    pass elimminates the error that you will get from not typing anything in the loop (#damn)

for num in for_list:
    if num == 3:
        continue            continue will skip the number 3 (in this example) and 'continue' the loop without the attached item
    print(num)

for num in for_list:
    if num == 3:
        break               break will just stop the loop from running at the condition
    print(num)



'Instead of writing this:'
my_list = "you are good"
for x in my_list:              -----> Instead of 4 lines we can reducs it to 1 line
    if x != ' ':
        print(x)


'We can do this:'

my_list = 'you are good'
y = [x for x in my_list]   ----->   allows us to shorten the for loops we are creating.
print(y)

y = [x for x in my_list]            y -> the name
                                    the first x is the action of the for loop
                                    the rest is the loop itself

y = [x for x in my_list if x!= " "]    we can also add an if to the loop. Which


def myfunc(my_string):
    new = ''
    for index, letter in enumerate(my_string):          enumerate(str) function allows us to break down a string, a list
        if index%2 == 0:                                    to the index (placement) of every letter inside our str
            new += letter.upper()
        else:
            new += letter
    return new

print(myfunc('maimoni'))

def myfunc(*args):
    for index,num in enumerate(args, start=1):          start=1 allows us to start the index at 1 instead of 0
        print(f"Index {index} -> {num}")

myfunc('apple', 'banana', 'pich')
#output
Index 1 -> apple
Index 2 -> banana
Index 3 -> pich



.                              '*args    and    *kwargs'

def myfunc(*args):          ---> *args allows us to create a tuple(list) of infinite items inside a function
    for x in args:                      {does not have to be '*args' it can be only '*' with a word like ('*or')}
        print(x)

myfunc(10,'hello',30)


def my_func(**kwarg):           ---> With the '**kwarg' command we can create an infinite items in the dictionary in our function
    for key,value in kwarg.items():                In addintion '**kwarg' can be exchange to '**or' if wanted
        print(key)
        print(value)
my_func(apple=100, banana=300)



                                   'def functions'

def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)             min() will return the lesser num in the ()
    else:
        return max(a,b)             max() will return the highest value num in the ()

print(myfunc(2,4))

