## SI 508 - HW2

## This assignment consists of building a number of complex functions that will interact with one another in some ways. It comes in a couple parts.

####################################################################
####### THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. ##########
import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f
####### END: THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. #####
####################################################################


### PART 1 - CAESAR CIPHER

## Explanation of a Caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher (You don't need to understand all of this to do this HW, but it will be useful background to have.)

## To complete this, you will need to check out the built-in Python functions ord() and chr() which are used to convert characters, in Python, to their numerical representations in the ASCII or UTF-8 encodings (ways that computers represent characters you type on the keyboard in the background), and from their numerical representations back to characters like 'A' and 'Z' and 'L', and so forth.

## You will be building a specific version of a Caesar cipher encoding/decoding algorithm. Note that this is NOT the only way to do so -- and in many ways, it may not be the "best" -- but we may come back to this along the way and look at how we might improve it. For now, we'll do it this way.

## You will build it up piece by piece, by implementing the functions as described below.

## [PROBLEM 0]
## PRACTICE: uncomment and try out the following code, and make sure you understand what it does.
## Recommend writing a comment after each line to convince yourself you know what each line is doing. You'll need these ideas for subsequent problems.
## GRADED: you must write at least 3 comments describing these lines of code and what they do, but if they are confusing at all -- which they are likely to be! -- I recommend writing a comment for every one.

s = "abcdEFGHIJK"
n = ord(s[1]) #s[1] = "b", ASCII decimal of b is 98
m = ord(s[-1]) #s[-1] = "K", ASCII decimal of K is 75
print(n) # n = 98
print(m) # m = 75
print(chr(n))
print(chr(m))
upp_s = s.upper() #upp_s = "ABCDEFGHIJK"
b = ord(upp_s[1]) # upp_s[1] = "B", ASCII decimal of B is 66
print(b) # b = 66
print(chr(b))
print(chr(90))
print(chr(65))
print(chr(60))
print(chr(90+4))
print(chr(26-12))
print(chr(90+4-26))
print(chr(26-12+26))


## [PROBLEM 1]
## Define a function called check_valid_input that will:
### - Accept a string input
### - If it is only one character, return True
### - If it is 0 characters (the empty string) or more than 1 character in the string, return False

def check_valid_input(strin):
    if len(strin) == 1:
        return True
    else :
        return False

## [PROBLEM 2]
## Define a function called crypt_char that will:
### - Accept as input a string new_string and a positive integer code_int that is less than 26.
### - Use check_valid_input to ensure the string is valid (you may assume only positive integers will be input for code_int, no floats or boolean values, etc)
### - If not valid input, print a message that says "Not valid single character!" and use the exit() function to end the program. If valid input, proceed with the rest of the function.
### - If the input character is punctuation (, ! ? . : ( ) { } [ ] ' ... you do not need to account or other possibilities than those, but you may if you wish), return the character itself as a one-character string
### - If the input character is a digit, return the character (digit) as a one-character string.
### - If the input character is a space, return the space character as a one-character string.
### - If the input character is alphabetical, convert the character to uppercase. Then, encrypt/decrypt this uppercase character by the amount of code_int. Finally, return the encrypted/decrypted character as a one-character string.
### - This should work for ANY positive integer above 0 and below 26.

### HINT: 90 is the integer representation in ASCII and utf-8 for the letter 'Z'. If a number is bigger than 90... you probably want to subtract 26 so that it's smaller than 90, to get a correct uppercase letter instead of another character! Similarly, 65 is the integer representation for the letter 'A'. If a number is less than 65, you probably want to add 26 so that it's larger than 65 and smaller than 90, to get a correct uppercase letter instead of another character!
### HINT: THIS function here in this problem is the crux of this whole part of the assignment. The others will rely on it and are (conceptually) somewhat simpler problems to solve.


## Remember to run it every time you finish a new part of it, and include debugging print statements at first, to try it out!

## Some sample invocations you can try the completed function with:
# print(crypt_char('A',3)) # Should print D
# print(crypt_char('a',3)) # Should print D
# print(crypt_char('z',2)) # Should print B
# print(crypt_char('Z',2)) # Should print B

def crypt_char(new_string, code_int):
    if check_valid_input(new_string) == False:
        print("Not valid single character!")
        exit()
    if ord(new_string) >= 20 and ord(new_string) <= 64:
        return new_string
    else:
        new_string = new_string.upper()
        new_code = ord(new_string) + code_int
        if new_code > 90:
            new_code -= 26
        if new_code < 65:
            new_code += 26
        return chr(new_code)


## [PROBLEM 3]
## Define a function called encrypt_message
### - Should accept a string input_string and a positive integer representing the amount to encrypt, enc_int, that must be less than 26. You may assume the integer will always be less than 26. Should also have an optional argument decrypt, with a default value of False
### - Should invoke the function crypt_char somewhere
### - If the decrypt parameter has the value False, should encrypt the whole input string, character by character.
### If the decrypt parameter has the value True, should multiple the positive integer less than 26 by -1 (to make it negative) and then encrypt in the normal way.
### - Should return the encrypted string.

## Remember to try invoking the function periodically as you work on it to test whether or not it works as you expect!
## Here are a just a couple sample invocations to try with the completed function. (Remember that this does NOT cover every possibility in the tests -- just some samples to help you think about the problem.)
# print(encrypt_message("hello, world!",3)) # should print: KHOOR, ZRUOG!
# print(encrypt_message("KHOOR, ZRUOG!",3,decrypt=True)) # should print: HELLO, WORLD!

def encrypt_message(input_string, enc_int, decrypt = False):
    y = ""
    if decrypt == True :
        enc_int *= (-1)
    for x in input_string:
        y += crypt_char(x, enc_int)
    return y


## [PROBLEM 4]
## Define a function called brute_force_caesar
### - Should accept one string, encrypted_msg, as input.
### - Should use a for loop and the encrypt_message function, always invoked with decrypt=True, to generate a list of possible decryptions of the input message.
### - Should return a list of strings, where each string in the list represents 1 possible decryption of the input string.

## Here's a sample invocation of this completed function you can try out.
# print(brute_force_caesar("KHOOR, ... ZRUOG! DQG VL 506!"))

def brute_force_caesar(encrypted_msg):
    possible_string = []
    for index in range(26):
        possible_string.append(encrypt_message(encrypted_msg, index, True))
    return possible_string

## [PROBLEM 5]
## Define a function called display_decryptions
## - Should accept one string, encrypted_msg, as input.
## - Should invoke the function brute_force_caesar to generate the resulting list.
## - Should then print each possible decryption on a separate line, with a "-" character preceding it, so a human could read the possible decryptions.
## - Each time running this function should generate 26 lines of output.
## Function should return None.

## For example, here's some example PARTIAL output of display_decryptions:
"""
    Message possibilities are as follows:
    - EXXEGO EX SRGI!
    - DWWDFN DW RQFH!
    - CVVCEM CV QPEG!
    - BUUBDL BU PODF!
    - ATTACK AT ONCE!
    - ZSSZBJ ZS NMBD!
    - YRRYAI YR MLAC!
    """ # etc -- 26 total lines of output

## Here's a couple sample invocation of this function to try with the completed version.
### ***** Uncomment these when you have completed the function ***** ###
######## DO NOT CHANGE THEM ######## ######## ######## ######## ########

# display_decryptions("BUUBDL BU PODF")
# display_decryptions("ATTACK")

######## ######## ######## ^ SEE ABOVE ######## ######## ######## ########

def display_decryptions(encrypted_msg):
    list_string = brute_force_caesar(encrypted_msg)
    print("Message possibilities are as follows:")
    for item in list_string:
        print("- " + item)

display_decryptions("BUUBDL BU PODF")
display_decryptions("ATTACK")

## PART 2 - OTHER FUNCTIONS

## [PROBLEM 6]
## Define a function called small_list that accepts a list of integers as input. You may assume the input will ALWAYS be a proper list of integers OR the empty list.
## The function should accumulate a list of only the integers in the input list larger than 5.
## The function should return that accumulated list.
## If the input list is the empty list, the function should return the empty list.

def small_list(lst_int):
    if lst_int == []:
        return []
    new_lst = []
    for integer in lst_int:
        if integer > 5:
            new_lst.append(integer)
    return new_lst


## [PROBLEM 7]
## Define a function called small_list_amount that accepts a list of integers as input AND a single integer lst_limit with a default value of 4.
## The function should accumulate a list of only the integers in the input list larger than five -- the first (integer input) many. So the returned list should be no longer than the input integer (though if there are fewer numbers > 5 than the input integer, it may be shorter).
## HINT: There are MANY ways you could do this ... the simplest involves building the whole list and then chopping it up.

def small_list_amount(lst_int, lst_limit = 4):
    if lst_int == []:
        return []
    
    for integer in lst_int:
        if integer > 5:
            first_index = lst_int.index(integer)
            break
    temp_lst = []

for integer in lst_int:
    if integer > 5:
        temp_lst.append(integer)
    
    if lst_limit >= len(temp_lst):
        return temp_lst
    else:
        new_lst = temp_lst[:lst_limit]
        return new_lst

## Here are some example invocations:
# print(small_list_amount([3,5,7,8,9,2,4,10,12],3))) # Should print and return the list: [7,8,9]
# print(small_list_amount([3,5,15,7,8,9,2,4,10,12],5)) # Should print and return the list: [15,7,8,9,10]
# print(small_list_amount([10,12,14,3],8)) # Should print and return the list: [10,12,14]


## HINT:  This will be easier if you do the following:
# - Check out how you solved problem 6
# - Write down a structure, in English, of how this function should work
# - Build it piece by piece
# - Careful not to "overthink" it! Is it much more complicated than Problem 6? Maybe barely at all...


####################################################################
####### THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. ##########
sys.stdout = orig_stdout
f.close()
####### END: THIS IS CODE TO SET UP TESTING. DO NOT CHANGE IT. #####
####################################################################

