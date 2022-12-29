from tkinter import *
from PIL import Image, ImageTk


# FII - AI Project
# Ciuta Andrei Calin
# Leagan Dan Adrian
# Tablan Andrei Razvan
# Volentir Alexandra


def faq():
    print("pressed the faq")


def home():
    print("pressed the home")


def match():
    print("pressed the match")

def alg():
    print("pressed the alg")


def start_app():
    root = Tk()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    image = (Image.open("picture.png"))
    resized_image = image.resize((480,370), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    Label(root, image=new_image, borderwidth=0).place(x=45, y=200)

    lines = (Image.open("lines.png"))
    resized_image_lines = lines.resize((309, 216), Image.ANTIALIAS)
    new_image_lines = ImageTk.PhotoImage(resized_image_lines)
    Label(root, image=new_image_lines, borderwidth=0).place(x=720, y=170)

    Label(root, text="TEST", borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 25')).place(x=600, y=500)
    Label(root, text="THE MOST REALISTIC", borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 25')).place(x=600, y=535)
    Label(root, text="COUPLE MATCHING APP", borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 25')).place(x=600, y=570)
    Label(root, text="NOW", borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 25 bold italic')).place(x=600, y=605)

    Label(root, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 16 bold')).place(x=450, y=730)

    home_btn = Button(root, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000',  font=('Montserrat 14 bold'), command=home)
    home_btn.place(x=600, y=50)
    faq_btn = Button(root, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000',  font=('Montserrat 14 bold'), command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(root, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=800, y=45)

    alg_img=PhotoImage(file="alg.png")
    alg_btn = Button(root, image=alg_img, borderwidth=0, bg="#FFBBBC", command=alg)
    alg_btn.place(x=550, y=320)

    root.mainloop()


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
    start_app()
    # solve_problem()
