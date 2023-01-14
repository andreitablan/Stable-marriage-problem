import random

N = 0
states = list()
solutions_bkt = list()
output_solutions = list()
count = 0
counter = 0


def if_stable(q_dict: list, col: int, mp, wp):
    for i in range(0, col):
        if q_dict[col] == q_dict[i]:
            return False

    for i in range(0, col):
        if (mp[i][q_dict[col]] < mp[i][q_dict[i]]) and (wp[q_dict[col]][i] < wp[q_dict[col]][col]):
            return False
        if (mp[col][q_dict[i]] < mp[col][q_dict[col]]) and (wp[q_dict[i]][col] < wp[q_dict[i]][i]):
            return False
    return True


def show(q_dict):
    global count
    count += 1
    for i in range(0, N):
        for j in range(0, N):
            if q_dict[i] == j:
                print("Man ", i, " is matched with woman ", j)


def get_state(q_dict, sol):
    global count
    state = dict()
    count += 1
    for i in range(0, N):
        for j in range(0, N):
            if q_dict[i] == j:
                state[i] = j
    return state, sol


def append_state(q_dict, sol):
    global states
    states.append((get_state(q_dict, sol)))


def append_to_output_possible_solutions(q_dict):
    global output_solutions
    global counter
    state = dict()
    counter += 1
    for i in range(0, N):
        for j in range(0, N):
            if q_dict[i] == j:
                state[str(i + 1)] = chr(ord('@') + j + 1)
    output_solutions.append(state)


def move(q_dict, i, mp, wp):
    # create state
    if i == N:
        append_state(q_dict, 1)
        solutions_bkt.append(get_state(q_dict, 1))
        append_to_output_possible_solutions(q_dict)
        return
    append_state(q_dict, 0)
    for j in range(0, N):
        q_dict[i] = j
        if if_stable(q_dict, i, mp, wp):
            move(q_dict, i + 1, mp, wp)


def bkt_approach(couples, mp, wp):
    global N
    global states
    global solutions_bkt
    global output_solutions
    global count
    global counter
    N = couples
    q = [0] * N
    states = list()
    solutions_bkt = list()
    output_solutions = list()
    count = 0
    counter = 0
    move(q, 0, mp, wp)
    N = 0
    return random.choice(output_solutions), 0
