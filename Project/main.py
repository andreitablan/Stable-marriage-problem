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


def update_states(states, men, women, man, woman, index_woman, index_man):
    states[man][index_woman] = 1
    states[woman][index_man] = 1

    for man_key in men.keys():
        if man_key != man:
            states[man_key][index_woman] = -1
    for woman_key in women.keys():
        if woman_key != woman:
            states[woman_key][index_man] = -1
    return states


def greedy_by_men(men, women, states):
    for key, value in men.items():
        for preference in value:
            index_woman = list(women).index(preference)
            index_man = list(men).index(key)
            if states[key][index_woman] == 0:
                states = update_states(states, men, women, key, preference, index_woman, index_man)
                break
    return states


def create_states(men, women):
    states = {}
    for key in men.keys():
        states[key] = [0 for x in range(0, len(women.keys()))]
    for key in women.keys():
        states[key] = [0 for x in range(0, len(men.keys()))]
    return states


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
    men = read_input("input_men.txt")
    women = read_input("input_women.txt")
    states = create_states(men, women)
    states = greedy_by_men(men, women, states)
    print(states)


if __name__ == '__main__':
    print('Welcome')
    solve_problem()
