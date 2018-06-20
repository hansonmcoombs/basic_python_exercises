# -*- coding: utf-8 -*-
"""
exercises to follow Basic Python Objects, Variables, and Operators, The Python List, and Dictionaries

Author: matth
Date Created: 7/06/2018 8:28 AM
"""
# this is an import statement, don't worry about it for now... it's simply here to help check your answers
import sys  # just ignore this it is for the exercises solution

sys.path.append('../exercises')  # just ignore this it is for the exercises solution
from solutions import check_exercise_1  # just ignore this it is for the exercises solution

test = 1
# exercise 1.1  Basic objects and operators

# problem 1.1.1 so about apple farming.  You have 10 workers, picking 8 hours a day and they can pick an average of 103 apples an hour
# please make a new variable 'num_picked' that has the value of the number of apples they have picked over the 5 day
# working week.

num_picked = 10 * 8 * 103 * 5

# problem 1.1.2 now you need to box them up, each box can hold 35 apples.  please create a new variable 'num_boxes' which has the
# number of boxes you will have at the end of the week.  note a fraction of a box does not makes sense.

num_boxes = num_picked // 35

# problem 1.1.3 finally please create a variable 'leftovers' which has the number of apples that are left over after boxing up.  again
# a fraction of an apple does not make sense.

leftovers = num_picked % 35

# problem 1.1.4 please create new variable 'destination' below which has a value of the largest town on the
# South Island of New Zealand, where the boxes of apples are going. Please print that variable and the number of
# boxes they should expect (the printing is not assessed).

destination = 'christchurch'

# exercise 1.2  The Python List

# the following variables are needed for the problems DO NOT MODIFY THESE

fruit_types = ['apples', 'cherries', 'blueberries', 'peaches']
nz_regional_councils = ["Bay of Plenty Regional Council", "Hawke's Bay Regional Council",
                        "Manawatu-Wanganui Regional Council", "Northland Regional Council",
                        "Taranaki Regional Council", "Waikato Regional Council", "Wellington Regional Council", ]
south_regional_councils = ["Canterbury Regional Council", "Otago Regional Council", "Southland Regional Council",
                           "West Coast Regional Council", ]
foods = {'peanut butter': 'jam', 'eggs': 'bacon', 'muslie': 'milk'}

# Problem 1.2.1 please create a new variable 'blue_fruit' that has the third item in the fruit types list
# ('blueberries') by list indexing

blue_fruit = fruit_types[2]

# Problem 1.2.2 Please create a new list 'better_fruits' that has all of the fruits except apples (please use list slicing)
better_fruits = fruit_types[1:]

# Problem 1.2.3 We just noticed that we forgot to add 'raspberries'.  please add it to the list and please do not type it into the
# list above.
fruit_types.append('raspberries')

# Problem 1.2.4 it turns out that all of the South Island Regional Councils were left off the nz_regional_councils list
# Luckily they're in teh south_regional_councils list. Please add them to the list (again without typing them in)
nz_regional_councils.extend(south_regional_councils)

# exercise 1.3 Dictionaries

# Problem 1.3.1 using the dictionary foods.  please create a variable 'to_by' which is what you would need to buy if you
# only had 'muslie'
to_buy = foods['muslie']

# problem 1.3.2 please add the pair ('pancakes', 'syrup') to the foods dictionary
foods['pancakes'] = 'syrup'

# below is an automated checking routine.  When you run the script it will give you feedback on your answers.
# if you make a mistake in your code that raises an exception (error) then you will have to fix that before you can
# check your answers
check_exercise_1(globals())  # don't worry about how this works for now
