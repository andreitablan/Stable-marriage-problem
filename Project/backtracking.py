from numpy import *
import time
import random

N = 0
states = list()
solutions_bkt = list()
output_solutions = list()
count = 0
counter = 1


def ok(q_dict: list, col: int, mp, wp):
    for i in range(0, col):
        if q_dict[col] == q_dict[i]:
            return False

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
                # print(state)
    output_solutions.append(state)


def move(q_dict, i, mp, wp):
    # create state
    if i == 3:
        append_state(q_dict, 1)
        # print("q", q_dict)
        solutions_bkt.append(get_state(q_dict, 1))
        append_to_output_possible_solutions(q_dict)
        # show(q_dict)
        return
    append_state(q_dict, 0)
    for j in range(0, N):
        q_dict[i] = j
        if ok(q_dict, i, mp, wp):
            move(q_dict, i + 1, mp, wp)


def bkt_approach(couples, mp, wp):
    global N
    N = couples
    q = [0] * N

    move(q, 0, mp, wp)
    time.sleep(3)
    return random.choice(output_solutions), 0


if __name__ == "__main__":
    mp = array([[0, 2, 1], [0, 2, 1], [1, 2, 0]])
    wp = array([[2, 1, 0], [0, 1, 2], [2, 0, 1]])
    print(bkt_approach(3, mp, wp))
