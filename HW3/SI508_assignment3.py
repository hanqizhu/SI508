## SI 508 - HW3
## A series of problems to practice data manipulation with files and new data structure(s)

## We've included among these files a couple text files. Each contains a bunch of text from a famous piece of writing.
## We have also included a test file, as usual.

#################
#### IMPORTS ####
#################
import csv

##########################
#### GLOBAL VARIABLES ####
##########################
### DO NOT CHANGE.
### A LIST OF ALL WORDS THAT SHOULD NOT COUNT FOR OUR LANGUAGE CALCULATIONS
STOPWORDS = [x.upper() for x in ["the","a","and","be","was","were","or","with",
"an","oh","this","in","of","on","at", "for", "to", "I", "you", "he", "she","they","her"
,"hers","his","theirs","be","was","is","were", "that", "it", "had","have","my",
"your","its","as","which","we","their", "them","but", "how","where", "not","from", "said",
"upon","there","been","me","by","one","would","no","yes","why","all",
"some","are","so","him","she","I'",'"I','very','could','if','whether','when',
'what','will','our',"has","out","who","mr.","mrs.","ms.","miss","into","man","up",
"do","can","may","son","then","did"]]

##########################
##########################

## [PROBLEM 1]
## Open the text file text1.txt and save the file reference in a variable f. Then save the contents of the file, all converted to uppercase (remember the .upper() string method!), in a string variable f_str_one, and close the file reference.

f = open("text1.txt","r")

f_str_one = f.read().upper()

f.close()

## [PROBLEM 2]
## Open the text file text2.txt and save the file reference in a variable f2. Then save the contents of the file, all converted to uppercase (remember the .upper() string method!), in a string variable f_str_two, and close the file reference.

f2 = open("text2.txt","r")

f_str_two = f2.read().upper()

f2.close()

## [PROBLEM 3]
## Find the most common word in the text1.txt file that is NOT in the STOPWORDS list. Save it in the variable common_text_one. Don't worry about punctuation in this file -- you can count all groups of non-whitespace characters as words.
## HINT: Use the dictionary accumulation pattern & the Max Value pattern to complete this problem!
## Suggestion: Write comments to plan out this solution step by step, and then translate your comments into code.


f1 = open("text1.txt","r")
data1 = f1.read().upper().split()
dict1 = {}
for x in data1:
    if x in dict1:
        dict1[x] += 1
    else :
        dict1[x] = 1
words1 = sorted(dict1, key=dict1.get, reverse=True)
use_words1 = []
for x in words1:
    if x not in STOPWORDS:
        use_words1.append(x)

common_text_one = use_words1[0]

f1.close()

## [PROBLEM 4]
## Find the most common word in the text2.txt file that is NOT in the STOPWORDS list. Save it in the variable common_text_two. Don't worry about punctuation in this file -- you can count all groups of non-whitespace characters as words.
## HINT: Use the dictionary accumulation pattern & the Max Value pattern to complete this problem!
## Suggestion: Write comments to plan out this solution step by step, and then translate your comments into code.

f3 = open("text2.txt","r")
data2 = f3.read().upper().split()
dict2 = {}
for x in data2:
    if x in dict2:
        dict2[x] += 1
    else :
        dict2[x] = 1
words2 = sorted(dict2, key=dict2.get, reverse=True)
use_words2 = []
for x in words2:
    if x not in STOPWORDS:
        use_words2.append(x)

common_text_two = use_words2[0]

f3.close()

## [PROBLEM 5]
## Define a function that accepts a filename (e.g. "text1.txt" ...) and returns the most common word (that is not one of the STOPWORDS) in the text of the file.
## HINT: Use the code you wrote in the last few problems to base this function on.
## NOTE: Make sure you handle the file correctly -- closing it and everything -- so you won't run into errors when you invoke the function (or in this file & tests! If you don't close the file correctly, you'll encounter trouble).
def find_most_common(filename):
    file = open(filename, "r")
    data = file.read().upper().split()
    file.close()
    dict = {}
    for x in data:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    words = sorted(dict, key=dict.get, reverse=True)
    use_words = []
    for x in words:
        if x not in STOPWORDS:
            use_words.append(x)

    return use_words[0]

## NOTE: You can test this function with the test file, of course, but also with your own test invocations that you can write here! If you run invocations to try out your function -- which we recommend -- TODO you should comment out the invocations before submitting this homework, to simplify your output!


## [PROBLEM 6]
## Define a function that accepts as input 1 string (you may assume there will be all uppercase letters in the string), and returns an integer representing the number of vowels in that string.
## Your function should define what vowels are: the letters AEIOU only.
def find_num_vowels(instr):
    instr = instr.upper()
    x = 0
    for ch in instr:
        if ch in "AEIOU": x += 1
    return x

## [PROBLEM 7]
## Open a CSV file for writing named text1_words.csv. You may use the CSV module OR "normal" file opening methods.

## Then, write into the text1_words.csv file three columns, with the following headers:
## WORD, OCCURRENCES, VOWELS
## The columns should contain, respectively:
## - Each word, ASIDE from stopwords, in the file text1
## - The number of times that word occurs in the file text1
## - The number of vowels that are in that word

## HINT: You can (and should!) rely on code you have written in earlier problems to help you complete this one!
with open('text1.txt', 'r') as f:
    data = f.read().upper().split()
    f.close()
    dict = {}
    for x in data:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    words = sorted(dict, key=dict.get, reverse=True)
    outfile = open("text1_words.csv", "w")
    outfile.write('WORD,OCCURRENCES,VOWELS\n')
    for x in words:
        if x not in STOPWORDS:
            row_string = '{},{},{}'.format(x, dict[x], find_num_vowels(x))
            outfile.write(row_string)
            outfile.write('\n')
    outfile.close()


## [PROBLEM 8]
## Perform the same operations you completed on text1 in PROBLEM 7 on text2. You should save these results in a file called text2_words.csv.
## NOTE: The file names are VERY important -- they are what the tests in our autograder will check against! They must be exactly correct.

with open('text2.txt', 'r') as f:
    data = f.read().upper().split()
    f.close()
    dict = {}
    for x in data:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    words = sorted(dict, key=dict.get, reverse=True)
    outfile = open("text2_words.csv", "w")
    outfile.write('WORD,OCCURRENCES,VOWELS\n')
    for x in words:
        if x not in STOPWORDS:
            row_string = '{},{},{}'.format(x, dict[x], find_num_vowels(x))
            outfile.write(row_string)
            outfile.write('\n')
    outfile.close()

## [PROBLEM 9]
## We've also included a CSV file -- called movies_dataset_group.csv.
## Open this up for reading with the CSV module.
## NOTE -- Don't worry, for this problem, about the *accuracy* of the data -- it's been edited (very) slightly to make it easier to manipulate for this HW. For now, your goal is to practice manipulation of the data so that later, you can use Python skills to consider other specifics and complete other types of data processing & manipulations.

## You have a few goals to achieve with this dataset for this assignment. To achieve them, you may use any methodology you want -- you may define functions, or not, etc. Whatever you like, as long as you achieve the aims specified, which we are testing for.
## HINT -- Remember to consider what datatype all the data is...
## The columns have the following headers: Title,US Gross,Worldwide Gross,US DVD Sales,Production Budget,Release Date,MPAA Rating,Running Time (min),Distributor,Source,Major Genre,Creative Type,Director,Rotten Tomatoes Rating,IMDB Rating,IMDB Votes

## GOALS from the MOVIES GROUP DATASET:

## [a] Create a dictionary saved in a variable world_gross that contains the title of a movie as the key, and as an associated value, the result of subracting that movie's US Gross amount from its Worldwide Gross amount. ("Gross" in this case means the amount of money EARNED by the movie's release -- people paying for it.)

import csv
with open('movies_dataset_group.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')

     world_gross = {}
     headers = []
     distributors_list = []
     for row in spamreader:
         if row[0] == "Title":
             headers = row
         else:
             world_gross[row[0]] = int(row[2]) - int(row[1])
             if row[8] not in distributors_list:
                 distributors_list.append(row[8])
## [b] Find the movie with the greatest difference between its worldwide gross and its U.S. gross. Save that movie's title in a variable called gross_diff.

     gross_diff = sorted(world_gross, key=world_gross.get, reverse=True)[0]

## [c] Create a list of the UNIQUE distributors of these movies. Save that list in a variable called distributors_list. (In other words, the list should have "Gramercy" in it only ONE time, "Universal" in it only one time, and so on for each different name that occurs in the DISTRIBUTORS column of this data.)

    #in [a]

csvfile.close()