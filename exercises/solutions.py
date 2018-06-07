# -*- coding: utf-8 -*-
"""
Author: matth
Date Created: 7/06/2018 8:28 AM
"""

from copy import deepcopy


def check_exercise_1(answers):
    points = 0
    possible_points = 0

    # section 1.1
    print('checking 1.1.1')
    possible_points += 1
    num_picked = 10 * 8 * 103 * 5
    if not 'num_picked' in answers.keys():
        print('you may have mis-named num_picked')
    elif answers['num_picked'] != num_picked:
        print('your answer for num_picked is not correct')
    else:
        print('good job your answer for num_picked is correct')
        points += 1

    print('checking 1.1.2')
    possible_points += 1
    correct_answer = int((10 * 8 * 103 * 5) / 35)
    var = 'num_boxes'
    if not var in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] != correct_answer:
        print('your answer for {} is not correct'.format(var))
    elif not isinstance(answers[var], int):
        print('{} is the wrong data type'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.1.3')
    possible_points += 1
    correct_answer = int((10 * 8 * 103 * 5) % 35)
    var = 'leftovers'
    if not var in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] != correct_answer:
        print('your answer for {} is not correct'.format(var))
    elif not isinstance(answers[var], int):
        print('{} is the wrong data type'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.1.4')
    possible_points += 1
    correct_answer = 'christchurch'
    var = 'destination'
    if var not in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var].lower() != correct_answer:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    # section 1.2
    print('checking 1.2.1')
    possible_points += 1
    var = 'blue_fruit'
    if var not in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] == 'peaches':
        print('your answer for {} is not correct, remember python is zero indexed'.format(var))
    elif answers[var] != 'blueberries':
        print('your answer for {} is not correct, remember python is zero indexed'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.2.2')
    possible_points += 1
    correct = ['cherries', 'blueberries', 'peaches']
    var = 'better_fruits'
    if var not in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] != correct:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.2.3')
    possible_points += 1
    correct = ['apples', 'cherries', 'blueberries', 'peaches', 'raspberries']
    var = 'fruit_types'
    if answers[var] != correct:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.2.4')
    nz_regional_councils = ["Bay of Plenty Regional Council", "Hawke's Bay Regional Council",
                            "Manawatu-Wanganui Regional Council", "Northland Regional Council",
                            "Taranaki Regional Council", "Waikato Regional Council", "Wellington Regional Council", ]
    south_regional_councils = ["Canterbury Regional Council", "Otago Regional Council", "Southland Regional Council",
                               "West Coast Regional Council"]

    possible_points += 1
    correct = deepcopy(nz_regional_councils)
    correct.extend(south_regional_councils)
    incorrect = deepcopy(nz_regional_councils)
    incorrect.append(south_regional_councils)

    var = 'nz_regional_councils'
    if answers[var] == incorrect:
        print('your answer for {} is not correct, we did not want a nested list'.format(var))
    elif answers[var] != correct:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    # section 1.3
    print('checking 1.3.1')
    possible_points += 1
    correct = 'milk'
    var = 'to_buy'
    if var not in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] != correct:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('checking 1.3.2')
    possible_points += 1
    correct = {'peanut butter': 'jam', 'eggs': 'bacon', 'muslie': 'milk'}
    correct['pancakes'] = 'syrup'

    var = 'foods'
    if var not in answers.keys():
        print('you may have mis-named {}'.format(var))
    elif answers[var] != correct:
        print('your answer for {} is not correct'.format(var))
    else:
        print('good job your answer for {} is correct'.format(var))
        points += 1

    print('you got {} out of {} points'.format(points, possible_points))
