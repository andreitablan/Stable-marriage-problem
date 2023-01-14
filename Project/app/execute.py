from tkinter import *
import random
from numpy import *
import time
import sys
from main import *
from Project.front.front import *
from Project.algo.bkt import *
from Project.algo.greedy import *
from Project.algo.utils import *


def commands():
    if number_of_arguments == 1:
        graphic_interface()
    elif sys.argv[1] == "-I":
        preferences_men = read_input(sys.argv[2])
        preferences_women = read_input(sys.argv[3])
        number_of_couples = len(preferences_men)
        greedy = False
        men_list = []
        women_list = []
        if sys.argv[4] == "greedy":
            greedy = True
        if greedy:
            start_time = time.time()
            men_list, women_list = solve_problem(number_of_couples, preferences_men, preferences_women, 'Greedy')
            end_time = time.time()
            print("The Greedy algorithm runs in ", end_time - start_time, " seconds.")
        else:
            start_time = time.time()
            men_list, women_list = solve_problem(number_of_couples, preferences_men, preferences_women, 'Backtracking')
            end_time = time.time()
            print("The Backtracking algorithm runs in ", end_time - start_time, " seconds.")
        print("The solution is:")
        print(men_list)

    elif sys.argv[1] == "-R":
        number_of_couples = int(sys.argv[2])
        preferences_men = {}
        preferences_women = {}
        list_of_men = []
        list_of_women = []
        for index in range(1, int(number_of_couples) + 1):
            list_of_men.append(str(index))
            list_of_women.append(chr(index + 64))
        for man in list_of_men:
            random.shuffle(list_of_women)
            preferences_men[man] = list(list_of_women)
        for woman in list_of_women:
            random.shuffle(list_of_men)
            preferences_women[woman] = list(list_of_men)
        print("Random preferences for men:")
        print(preferences_men)
        print("Random preferences for women:")
        print(preferences_women)
        greedy = False
        men_list = []
        women_list = []
        if sys.argv[3] == "greedy":
            greedy = True
        if greedy == True:
            start_time = time.time()
            men_list, women_list = solve_problem(number_of_couples, preferences_men, preferences_women, 'Greedy')
            end_time = time.time()
            print("The Greedy algorithm runs in ", end_time - start_time, " seconds.")
        else:
            start_time = time.time()
            men_list, women_list = solve_problem(number_of_couples, preferences_men, preferences_women, 'Backtracking')
            end_time = time.time()
            print("The Greedy algorithm runs in ", end_time - start_time, " seconds.")
        print("The solution is:")
        print(men_list)

    else:
        print("Please type one of the following commands:")
        print("main.py -I <input_men.txt> <input_women.txt> greedy")
        print("main.py -I <input_men.txt> <input_women.txt> bkt")
        print("main.py -R <number_of_people greedy")
        print("main.py -R <number_of_people> bkt")


def solve_problem(number_of_couples, preferences_men, preferences_women, solving_metho):
    men = create_person_list(preferences_men)
    women = create_person_list(preferences_women)

    if solving_metho == 'Greedy':
        return greedy_approach(men, women, preferences_men, preferences_women)
    else:
        mp, wp = create_bkt_preferences(preferences_men, preferences_women)
        solutie1, solutie2 = bkt_approach(int(number_of_couples), mp, wp)
        return solutie1, solutie2


def read_input(path):
    preferences = {}
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    for line in lines:
        person = line.split(":")
        preference_by_person = person[1].split(",")
        preferences[person[0]] = preference_by_person
    file.close()
    return preferences
