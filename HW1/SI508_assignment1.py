## SI 508 - HW1
## A series of problems to practice fundamental Python programming techniques

### There are TWO parts to this assignment:
## (1) Completing the code problems in this file.
## Run TESTS_SI508_assignment1.py to view the test output.
## Your output might look like this when ALL tests pass: https://www.dropbox.com/s/f6r6txdv5vdba0s/Screenshot%202018-08-31%2013.08.55.png?dl=0

## NOTE that for this homework assignment, printed output will not show up in the console -- it will show up in a file called out.txt, in the folder where this assignment is saved. Saving the output in a file allows us to test it! If you want to see what is printing out, you can check out that file that will be generated after you run this assignment.

## (2) Write a .txt file with no more than 2 short bulletpoints summarizing: something that was difficult OR something you learned OR something that surprised you about each problem. Save this file as SI508_A1_summary.txt, and submit this file along with your completed SI508_assignment1.py.

## IMPORTANT NOTE: Make sure to save your files as the names you are given -- e.g. you must submit this edited file as SI508_assignment1.py -- no changes. This is what allows us to use our grading system on it!

####################################################################
####### THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. ##########
import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
####### END: THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. #####
####################################################################


## [PROBLEM 1]
print("\n*** PROBLEM 1 ***\n") # Lines like this exist for clarity when you run the program. You should leave them alone.

## Write code to assign the number of CHARACTERS in the value of rv to a variable called num_chars.
## Then write code to assign the number of WORDS in the value of rv (as we humans understand words) to a variable called num_words.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

## Write your code for Problem 1 here:

num_chars = len(rv)
#print(num_chars)
words = rv.split()
num_words = len(words)
#print(num_words)

## [PROBLEM 2]
print("\n*** PROBLEM 2 ***\n")
## We've provided code that assigns a couple sequences to variables, below. To complete this problem, you should complete the following tasks by writing some additional code.
# NOTE: Keep in mind: All ordinal numbers in instructions, like “third” or “fifth” refer to the way HUMANS count. How do you write code to find the right things?

num_lst = [4,16,25,9,100,12,13]
mixed_bag = ["hi", 4,6,8, 92.4, "see ya", "23", 23]

# (a) Assign the value of the third element of num_lst to a variable called third_elem.

third_elem =  num_lst[2]
#print(third_elem)

# (b) Assign the value of the sixth element of num_lst to a variable called elem_sixth.

elem_sixth = num_lst[5]
#print(elem_sixth)

# (c) Assign the length of num_lst to a variable called num_lst_len.

num_lst_len = len(num_lst)
#print(num_lst_len)

# NOTE: Consider: what is the difference between mixed_bag[-1] and mixed_bag[-2] (you may want to print out those values or print out information about those values, so you can make sure you know what they are!)?

# (d) Write code to print out the type of the third element of mixed_bag.

print(mixed_bag[2])

# (e) Write code to assign the type of the fifth element of mixed_bag to a variable called fifth_type.

fifth_type = type(mixed_bag[4])
#print(fifth_type)

# (f) Write code to assign the type of the first element of mixed_bag to a variable called another_type.

another_type = type(mixed_bag[0])
#print(another_type)

# Write your code here / below each of the respective comments.

## [PROBLEM 3]
print("\n*** PROBLEM 3 ***\n")

## Below are a few function definitions in Python. You do NOT need to understand what this code does in its entirety yet. But you should be able to use it, as directed:

## - Write code that assigns to the variable func_var the function greeting (*without* executing the function).

## - Then, write code that assigns to the variable new_digit the return value from *executing* the function random_digit.

## - Then, write code that assigns to the variable digit_func the function random_digit (without executing the function).

## HINT: You MAY find this problem "easier" than you expect it to be. Try not to second-guess yourself too much!

### PROVIDED CODE ###
def square(num):
    return num**2

def greeting(st):
    st = str(st) # just in case
    return "Hello, " + st

def random_digit():
    import random
    return random.choice([0,1,2,3,4,5,6,7,8,9])

def add_lengths(str1, str2):
    return len(str1) + len(str2)
### END PROVIDED CODE ###

## Write code for Problem 3 here.

func_var = greeting
new_digit = random_digit()
digit_func = random_digit

## [PROBLEM 4]
print("\n*** PROBLEM 4 ***\n")

# How many characters are in each element of list lp? Write code to print the length (number of characters) of each element of the list, on a separate line. (Do not write 8+ lines of code to do this. Use a for loop.)

# The output you should see when you run this program should be:
#
# 5
# 13
# 11
# 12
# 3
# 12
# 11
# 6
# Use iteration (a for loop).

lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]

## Write code for Problem 4 here.

for x in lp:
    print(len(x))

## [PROBLEM 5]
print("\n*** PROBLEM 5 ***\n")

## Write one line of code to assign a list containing only the third through fifth elements of whoa_list (as humans count, so [4, 6.0, 7.5]) to a variable some_of_list. You must use slicing and you must refer to whoa_list in your code.

## HINT: Remember the rules of slicing and indices of sequences in Python! Also remember that the type of some_of_list should be a list when you are done running your code!

whoa_list = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

## Write your code for Problem 5 here.

some_of_list = whoa_list[2:5]
#print(some_of_list)

## [PROBLEM 6]
print("\n*** PROBLEM 6 ***\n")

# Write code that uses iteration to print out each element of the list stored in excited_words, BUT print out each element without its ending punctuation. You should see:
#
# hello
# goodbye
# wonderful
# I love Python
# (Hint: remember string slicing?)

excited_words = ["hello!", "goodbye!", "wonderful!", "I love Python?"]

## Write code for Problem 6 here.

for h in excited_words:
    h = h[:-1]
    print(h)

## [PROBLEM 7]
print("\n*** PROBLEM 7 ***\n")

## Use the built-in Python function called range and an operation on string data to generate the following printed output:

## hello
## hello!
## hello!!
## hello!!!
## hello!!!!

## Write your code for problem 7 here.

for x in range(5):
    print("hello" + x * "!")

## [PROBLEM 8]
print("\n*** PROBLEM 8 ***\n")
## Write code, using the accumulation pattern, to iterate over new_string and accumulate a new string in a variable called exclam_string with an exclamation point (!) after each of the characters. It should look like this: h!i! !e!v!e!r!y!o!n!e!. You must use the accumulation pattern – do not hard-code.

new_string = "hi everyone"

## Write code for Problem 8 here.

exclam_string = ""
for x in new_string:
    exclam_string += (x + "!")
#print(exclam_string)

## [PROBLEM 9]
print("\n*** PROBLEM 9 ***\n")

## Below is a dictionary diction with two key-value pairs inside it. The string "python" is one of its keys. Using dictionary mechanics, print out the value of the key "python".

diction = {"python":"you are awesome","autumn":100}

## Write your code for Problem 9 here.

print(diction['python'])

## [PROBLEM 10]
print("\n*** PROBLEM 10 ***\n")

## Below is an empty dictionary saved in the variable nums, and a list saved in the variable many_numbers. Use iteration and dictionary mechanics to add each element of many_numbers as a key in the dictionary nums. Each key should have the value 0.

## The dictionary should end up looking something like this when you print it out (remember, you can’t be sure of the order):
## {"two":0,"three":0,"four":0,"eight":0,"seventeen":0,"not_a_number":0}

## You should not change either of the lines of code that is provided for this problem.
## HINT: You can do this by adding just two more lines of code!

nums = {}
many_numbers = ["two","three","four","seventeen","eight","not_a_number"]
# Write your code for Problem 10 here.

for x in many_numbers:
    nums[x] = 0
#print(nums)

## [PROBLEM 11]
print("\n*** PROBLEM 11 ***\n")

## Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

## HINT 1: Use the accumulation pattern!
## HINT 2: the in operator checks whether a substring is present in a string.

items = ["whirring", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

# Write your code for Problem 11 here.

acc_num = 0
for x in items:
    if 'w' in x: acc_num += 1
#print(acc_num)

## [PROBLEM 12]
print("\n*** PROBLEM 12 ***\n")
## Check out the provided code in Problem 3 and the Functions information in the textbook. Using those as guidelines, define a function called subtract_three that takes an integer as input and returns that same value, minus 3.

## Write your code for problem 12 here.

def subtract_three(num):
    return num - 3

## [PROBLEM 13]
print("\n*** PROBLEM 13 ***\n")
## Using what you learned in Problem 12, define another function in Python called add_greeting: this function should return None, but it should take 1 string as input and print out a string that concatenates "HELLO " to the beginning of that string. For example,

## If you were to run: add_greeting("SI 506")
## You should see printed out: HELLO SI 506
## If you were to run: add_greeting("   everyone")
## You should see printed out: HELLO    everyone
## If you were to run: print(add_greeting("errbody")
## You should see printed out the following 2 lines:
## HELLO errybody
## None

# Write your code for Problem 13 here.

def add_greeting(name):
    print("HELLO " + name + '\n')

## [PROBLEM 14]
print("\n*** PROBLEM 14 ***\n")

## Below we have provided some code, commented out.
## If you un-comment it, you will find that it does not work.

## How can you fix it so that it passes the tests for Problem 14?
## Write a sentence or two in a comment about what is wrong with this code and why.
## Then, un-comment the code and debug it so that it does pass the tests. (Remember -- change one thing at a time, then try it out!)

## Write your comment about what's goin on in this code here: COMMENT GOES BELOW THIS LINE!

## Then un-comment and fix the code below. Please do NOT delete the existing comments in this problem (above this line).

# amounts = ["$5.64", "apples","pears","lemons", "$7.82","tuna","tofu", "$0.51","paper", "thread"]
# five_dollar = amounts["$5.64"]
# cheap_things = amounts["$0.51"]

amounts = {"$5.64":["apples","pears","lemons"], "$7.82":["tuna","tofu"], "$0.51":["paper", "thread"]}
five_dollar = amounts["$5.64"]
cheap_things = amounts["$0.51"]


####################################################################
####### THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. ##########
sys.stdout = orig_stdout
f.close()
####### END: THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. #####
####################################################################

