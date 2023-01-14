from numpy import *
from Project.algo.greedy import *
from Project.algo.bkt import *


def create_person_list(dictionary):
    list_of_people = []
    for key in dictionary.keys():
        list_of_people.append(key)
    return list_of_people


def create_bkt_preferences(preferences_men, preferences_women):
    males = []
    women = []
    for key, values in preferences_men.items():
        women_list = []
        for value in values:
            woman = ord(value) - 65
            women_list.append(woman)
        males.append(women_list)
    for key, values in preferences_women.items():
        men_list = []
        for value in values:
            if value != '10':
                man = ord(value) - 49
                men_list.append(man)
            else:
                man = 10
                men_list.append(man)
        women.append(men_list)
    mp = array(males)
    wp = array(women)
    return mp, wp


def solve_problem(number_of_couples, preferences_men, preferences_women, solving_metho):
    men = create_person_list(preferences_men)
    women = create_person_list(preferences_women)

    if solving_metho == 'Greedy':
        return greedy_approach(men, women, preferences_men, preferences_women)
    else:
        mp, wp = create_bkt_preferences(preferences_men, preferences_women)
        solutie1, solutie2 = bkt_approach(int(number_of_couples), mp, wp)
        return solutie1, solutie2