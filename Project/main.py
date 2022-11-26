# FII - AI Project
# Ciuta Andrei Calin
# Leagan Dan Adrian
# Tablan Andrei Razvan
# Volentir Alexandra

'''
class Person:
    def __init__(self, id, preferences, count):
        self.id = id
        self.married = False
        self.preferences = preferences
        self.state = [0 for x in range(0, count)]

    def set_married(self):
        self.married = True
'''


def is_stable(states, preferences_men, preferences_women, men, women):
    wives = []
    for man1 in preferences_men.keys():
        for man2 in preferences_men.keys():
            for index in range(0, len(states[man1])):
                if states[man1][index] == 1:
                    woman = women[index]
                    print(man1, ' ', woman)


def update_states(states, preferences_men, preferences_women, man, woman, index_woman, index_man):
    states[man][index_woman] = 1
    states[woman][index_man] = 1

    for man_key in preferences_men.keys():
        if man_key != man:
            states[man_key][index_woman] = -1
    for woman_key in preferences_women.keys():
        if woman_key != woman:
            states[woman_key][index_man] = -1
    return states


def greedy_by_men(states, preferences_men, preferences_women):
    for key, value in preferences_men.items():
        for preference in value:
            index_woman = list(preferences_women).index(preference)
            index_man = list(preferences_men).index(key)
            if states[key][index_woman] == 0:
                states = update_states(states, preferences_men, preferences_women, key, preference, index_woman,
                                       index_man)
                break
    return states


def create_states(preferences_men, preferences_women):
    states = {}
    for key in preferences_men.keys():
        states[key] = [0 for x in range(0, len(preferences_women.keys()))]
    for key in preferences_women.keys():
        states[key] = [0 for x in range(0, len(preferences_men.keys()))]
    return states


def create_person_list(dictionary):
    list_of_people = []
    for key in dictionary.keys():
        list_of_people.append(key)
    return list_of_people


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


def solve_problem():
    preferences_men = read_input("input_men.txt")
    preferences_women = read_input("input_women.txt")
    men = create_person_list(preferences_men)
    women = create_person_list(preferences_women)
    states = create_states(preferences_men, preferences_women)
    states = greedy_by_men(states, preferences_men, preferences_women)
    print(states)
    is_stable(states, preferences_men, preferences_women, men, women)


if __name__ == '__main__':
    print('Welcome')
    solve_problem()
