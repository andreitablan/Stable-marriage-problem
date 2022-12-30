from tkinter import *

from PIL import Image, ImageTk

# FII - AI Project
# Ciuta Andrei Calin
# Leagan Dan Adrian
# Tablan Andrei Razvan
# Volentir Alexandra

root = Tk()
f1 = Frame(root)
f2 = Frame(root)


def faq():
    print("pressed the faq")


def home():
    print("pressed the home")


def match():
    print("pressed the match")


def raise_frame(frame):
    frame.tkraise()


def description_page():
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f2.configure(bg='#FFBBBC')


    Label(f2, text="How is our app working", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').pack(
        side=TOP, anchor=W, padx=100, pady=130)
    Label(f2,
          text="➊ First the user sends the input using the graphic interface, choosing the boys\nand girls, their " +
               "preferences and which algorithm our app should use\n(Greedy or Backtracking).\n\n➋ Second, the program " +
               "runs the algorithm for the given instance and finds a \nresult, considering every person's preferences." +
               "\n\n➌ Finally, the result is displayed on the app's screen.",
          borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 20'), justify=LEFT).pack(side=LEFT, anchor=N,
                                                                                                padx=50, pady=0)
    back_arrow = PhotoImage(file="back_arrow.png")

    #back_btn = Button(f2, text="Back", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
    #                 image=back_arrow,command=start_app,relief=SUNKEN,highlightthickness=0,highlightcolor="#FFBBBC",highlightbackground="#FFBBBC", overrelief=SUNKEN)

    back_btn = Button(f2, text="Back", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      image=back_arrow,command=start_app)
    back_btn.place(x=30, y=30)
    raise_frame(f2)
    root.mainloop()


def start_app():
    for frame in (f1, f2):
        frame.grid(row=0, column=0, sticky='news')

    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f1.configure(bg='#FFBBBC')
    image = (Image.open("picture.png"))
    resized_image = image.resize((480, 370), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    Label(f1, image=new_image, borderwidth=0).place(x=45, y=200)

    lines = (Image.open("lines.png"))
    resized_image_lines = lines.resize((309, 216), Image.ANTIALIAS)
    new_image_lines = ImageTk.PhotoImage(resized_image_lines)
    Label(f1, image=new_image_lines, borderwidth=0).place(x=720, y=170)

    Label(f1, text="TEST", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25').pack(padx=600, pady=500)
    Label(f1, text="THE MOST REALISTIC", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25').place(x=600,
                                                                                                                  y=535)
    Label(f1, text="COUPLE MATCHING APP", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25').place(
        x=600, y=570)
    Label(f1, text="NOW", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold italic').place(x=600,
                                                                                                               y=605)

    Label(f1, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=450,
                                                                                                                y=730)

    home_btn = Button(f1, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.place(x=600, y=50)
    faq_btn = Button(f1, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f1, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)

    alg_img = PhotoImage(file="alg.png")
    alg_btn = Button(f1, image=alg_img, borderwidth=0, bg="#FFBBBC", command=description_page)
    alg_btn.place(x=550, y=320)

    raise_frame(f1)
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
