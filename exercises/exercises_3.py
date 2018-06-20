# -*- coding: utf-8 -*-
"""
Exercises to follow: Functions in Python

Author: matth
Date Created: 19/06/2018 4:00 PM
"""

# !!! To import the data you must run the lines of code from here
# this is an import statement, don't worry about it for now... it's simply here to help check your answers and provide
# some data
import sys  # just ignore this it is for the exercises solution
sys.path.append('../exercises')  # just ignore this it is for the exercises solution
from solutions import check_exercise_3, wells, sd150, sd7  # just ignore this it is for the exercises solution

# !!! To here.

# exercise 3.1
# In exercise 2.3 we did a stream depletion assement:
#        exercise 2.3
#        we have a number of groundwater abstraction bores which are near to rivers "wells".  We need you to assess how connected the
#        groundwater is to the river.  For our purposes we have four different levels of connection based on the percentage of
#        the groundwater derived from the river after 7 days (provided in "sd7") and after 150 days (provided in "sd150") the
#        four different levels are:
#                                  'direct': where sd7 is >=90%
#                                  'high': where sd7 is <90% and sd150 >= 60%
#                                  'moderate': where sd7 is <90% and 40% <= sd150 < 60%
#                                  'low': where sd7 is <90% and sd150 < 40%
#        you are given a list of well numbers ("wells") and dictionaries of the stream depletion after 7 days "sd7" and after
#        150 days ("sd150"), please calculate the stream depletion for each well and add it to the dictionary "sd_assesments"
#        note that this is based on real data from Enviroment Canterbury, but the wells have been randomised.
#        "sd7", "sd150", and "wells" are imported from another script, to import them into your consol, please run the lines
#        of code between the !!!
# please complete the function below. We have included the "sd7", "sd150", and "wells" object in the import statement
# at the top of the script to help you check your work as you go. Hint: you can get the wells list from either "sd7" or "sd150"

def calc_sd(sd7s, sd150s):
    """
    calculates the connectivity between a well and a stream given the stream depletion calculations at 7 and 150 days
    :param sd7s: dictionary of form: {well_number: sd7}
                 where sd7 is the stream depletion percentage after 7 days
    :param sd150s: dictionary of form: {well_number: sd150}
                   where sd150 is the stream depletion percentage after 150 days
    :return: a dictionary of {well_number: connection_level} connection level is one of 'direct', 'high', 'moderate', 'low'
    """
    pass  #remember this just says do nothing... you will have to fix this


# below is an automated checking routine.  When you run the script it will give you feedback on your answers.
# if you make a mistake in your code that raises an exception (error) then you will have to fix that before you can
# check your answers
check_exercise_3(globals())  # don't worry about how this works for now
