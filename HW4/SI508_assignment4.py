# -*- coding: utf-8 -*-
## SI 508 - HW4
## A series of problems to practice accessing, using, and manipulating structured data

## NOTE that print statements are not redirected to a file for this assignment -- because none of the required output is printed. You may certainly want to use print statements for your own understanding and debugging!

## NOTE also that while it is possible to pass tests by hard-coding answers (of course), doing so will ultimately NOT count for points even if the autograder passes. For example, if you were to type out a correct JSON file by hand and not write code to do it, that would not earn points. You should work on this with a goal of going through the correct code processes to get the desired results.

## PROVIDED FILES:
# - This file, SI508_assignment4.py
# - samplepost.json
# - scores.csv
# - Test file: TESTS_SI508assignment4.py


#################
#### IMPORTS ####
#################
import csv
import json
import requests


## [PROBLEM 1]
## This problem has one goal which you'll need to separate into a few parts to complete.

## We've provided a .json file called samplepost.json.
## The file contains a (edited) representation of a Facebook post from a few years ago. (The way of accessing data from Facebook has changed since the time this data was retrieved! But the data is still structured in a fine way.)
## This data represents a Facebook post with a photo, and a number of likes and comments.

## Your goal is to take this .json file, open it, and use the data in it (specifically, the data about comments on the post) to create a CSV file.
## The CSV file you create should be called post_data.csv.
## Its headers should be:
### CREATED_TIME, COMMENT_TEXT, NAME_OF_POSTER, NUM_LIKES, NUM_WORDS

## The column under CREATED_TIME in each row should contain a representation of the time at which a given comment was posted.
## The column under COMMENT_TEXT in each row should contain the text of the comment. (CAREFUL: You'll want to make sure there are no newlines in the text so you don't mess up the formatting of the file!)
## The column under NAME_OF_POSTER should contain the name of the user who posted the comment (e.g. "P Resnick").
## The column under NUM_LIKES should contain an integer representing the number of likes htat have been given to the comment on Facebook. (Number of people who clicked "like" on this comment, which is represented in the data.)
## The column under NUM_WORDS should contain an integer representing the number of words (chunks of visible characters separated by spaces) that are in the text of the comment.

## Of course, there should be one row in the CSV file per each comment in the post (whose data is provided in samplepost.json).





## [PROBLEM 2]
## Given the CSV file called scores.csv, which we have provided, you should open the file, and use the data to:

# (1) Save the data in a Python dictionary called scores_diction,of the following format:

## The keys should each correspond to one value in the NAME column of the CSV file, and each key's associated value should be a list that contains each of the values in the subsequent columns, in the same row.

# And (2), create a new valid .json file called scores_names.json with the data in that Python dictionary.

## For example, one key-value pair in the data should be as follows (from the first line of the CSV file):
## "Student 3457":[78,89,92,81]

## Recap of your goal for this problem : The data from the scores.csv CSV file should be reorganized into a Python dictionary format and saved in scores_diction, and that dictionary should be saved as a .json file you create: scores_names.json






## [PROBLEM 3]
## We've provided a function definition that makes a request to the iTunes Search API (DOCS: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) based on search input, retrieves data, and returns a Python object representing that data. The function is called get_itunes_data -- below.

## NOTE that this function can only be invoked on the same computer a couple hundreds of times a day, or fewer. Be careful, if you are going to run this program more frequently than that, that you comment out any invocations the function and think about your plan / work on the other two problems first.

## Your goal for this problem is to:
# - invoke get_itunes_data on a couple of different inputs and save the results in variables (try it out and see what it does)
# - uncomment the provided invocations of the function below, with inputs "janelle monae" and "the beatles". From each of those invocations, you'll get a bunch of data, which you should save in variables.
# Use the data from EACH of those inputs to create two lists:
## The variable jm_lst should contain a list of the item names that result from this search on "janelle monae" on iTunes, and
## The variable beatles_lst should contain a list of the item names that result from this search on "the beatles" on iTunes

def get_itunes_data(search_term):
    baseurl = "https://itunes.apple.com/search"
    params_diction = {}
    params_diction["term"] = search_term
    resp = requests.get(baseurl, params=params_diction)
    all_data = json.loads(resp.text)
    return all_data

## Perform other invocations and/or data investigation here!


## The sample invocations for your results -- you will need to uncomment these and use them / assign their results to variables...
#get_itunes_data("janelle monae")
#get_itunes_data("beatles")
