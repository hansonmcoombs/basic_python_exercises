# -*- coding: utf-8 -*-
"""
exercises to follow: Conditional Statements and Loops in Python
Author: matth
Date Created: 19/06/2018 3:43 PM
"""

# !!! To import the data you must run the lines of code from here
# this is an import statement, don't worry about it for now... it's simply here to help check your answers and provide
# some data
import sys  # just ignore this it is for the exercises solution
sys.path.append('../exercises')  # just ignore this it is for the exercises solution
from solutions import check_exercise_3, sd7, sd150, wells  # just ignore this it is for the exercises solution

# !!! To here.

# default datasets (do not change these!)
bills = [13.10, 25.40, 35.78, 5.75, 6.97]

n_leaching_rate = [43, 25, 10, 13, 59, 8, 20, 30, 54, 61, 49, 32, 66, 44, 60, 21, 12, 27, 13, 45, 6, 16, 27, 54, 55, 25,
                   41, 30, 34, 8, 66, 28, 42, 32, 47, 55, 15, 59, 34, 32, 21, 53, 32, 59, 25, 5, 30, 24, 36, 40, 43, 35,
                   63, 26, 64, 14, 68, 60, 60, 23, 32, 52, 44, 29, 29, 51, 29, 51, 5, 68, 55, 56, 45, 66, 11, 52, 67,
                   12, 7, 28, 63, 22, 33, 6, 33, 67, 33, 11, 9, 12, 51, 64, 56, 69, 12, 60, 17, 20, 38, 19, 12, 22, 54,
                   49, 52, 33, 12, 30, 66, 59, 57, 32, 12, 61, 47, 44, 21, 13, 48, 8, 62, 59, 33, 24, 49, 31, 17, 49,
                   23, 37, 7, 42, 15, 20, 26, 35, 48, 45, 15, 51, 36, 40, 63, 50, 50, 69, 14, 44, 69, 8]

# exercise 3.1
# you own a restaurant and you've got a set of "bills" for your diners tonight, but you forgot to add sales tax onto
# their bills.  please use a loop to add the 15% sales tax onto their final bill and add that new value to the
# bills_with_gst list below:
bills_with_gst = []

# exercise 3.2
# You have been tasked to separate a group of farms into 3 classes: 'low_emitter', 'moderate_emitter' and 'high_emitter'
# (case sensitive, as you know) based on their n leaching rates (provided in the "n_leaching_rate" variable above.
# where a farm is leaching less than 10 kg/ha/yr they are a 'low_emitter', where a farm is leaching 10 - 35 kg/ha/yr
# (inclusive) it is classed as a 'moderate_emitter', finally if they are leaching more than 35 kg/ha/yr then they are
# classed as a 'high_emitter'.  Please add each farms classification into the empty list "farm_emission_profiles" below
farm_emission_profiles = []

# exercise 3.3
# we have a number of groundwater abstraction bores which are near to rivers "wells".  We need you to assess how connected the
# groundwater is to the river.  For our purposes we have four different levels of connection based on the percentage of
# the groundwater derived from the river after 7 days (provided in "sd7") and after 150 days (provided in "sd150") the
# four different levels are:
#                           'direct': where sd7 is >=90%
#                           'high': where sd7 is <90% and sd150 >= 60%
#                           'moderate': where sd7 is <90% and 40% <= sd150 < 60%
#                           'low': where sd7 is <90% and sd150 < 40%
# you are given a list of well numbers ("wells") and dictionaries of the stream depletion after 7 days "sd7" and after
# 150 days ("sd150"), please calculate the stream depletion for each well and add it to the dictionary "sd_assesments"
# note that this is based on real data from Enviroment Canterbury, but the wells have been randomised.
# "sd7", "sd150", and "wells" are imported from another script, to import them into your consol, please run the lines
# of code between the !!!
sd_assesments = {}

# below is an automated checking routine.  When you run the script it will give you feedback on your answers.
# if you make a mistake in your code that raises an exception (error) then you will have to fix that before you can
# check your answers
check_exercise_3(globals())  # don't worry about how this works for now
