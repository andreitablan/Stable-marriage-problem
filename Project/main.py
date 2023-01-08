from tkinter import *
import random
from PIL import Image, ImageTk
from numpy import *
import os
import time

# FII - AI Project
# Ciuta Andrei Calin
# Leagan Dan Adrian
# Tablan Andrei Razvan
# Volentir Alexandra

root = Tk()
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)


def raise_frame(frame):
    frame.tkraise()


def show_solution(solution, number_of_couples, solving_method):
    # print(solution)
    for widgets in f6.winfo_children():
        widgets.destroy()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f6.configure(bg='#FFBBBC')

    home_btn = Button(f6, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.pack(padx=590, pady=50)

    faq_btn = Button(f6, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f6, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)
    title = "The solution using " + solving_method + " is:"
    Label(f6, text=title, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=300, y=100)
    y_man = 200
    y_woman = 200
    men_images = []
    women_images = []
    for key, value in solution.items():
        man_image = PhotoImage(file="man1.png")
        Label(f6, text=key, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 15 bold', image=man_image,
              compound='center').place(x=350, y=y_man)
        y_man = y_man + 50
        men_images.append(man_image)
        Label(f6, text="is married to", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(
            x=450,
            y=y_woman + 5)
        woman_image = PhotoImage(file="woman1.png")
        Label(f6, text=value, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 15 bold',
              image=woman_image, compound='center').place(x=650, y=y_woman)
        y_woman = y_woman + 50
        women_images.append(woman_image)

    Label(f6, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=450,
                                                                                                              y=730)

    raise_frame(f6)
    root.mainloop()


def input_from_user_is_correct(preferences_men, preferences_women, number_of_couples):
    men_correct = []
    women_correct = []

    for index in range(1, int(number_of_couples) + 1):
        men_correct.append(str(index))
        women_correct.append(str(chr(index + 64)))
    men_correct.sort()
    women_correct.sort()

    for man, list_of_preferences in preferences_men.items():
        new_list=list_of_preferences.copy()
        new_list.sort()
        if new_list != women_correct:
            return False
    for woman, list_of_preferences in preferences_women.items():
        new_list = list_of_preferences.copy()
        new_list.sort()
        if new_list != men_correct:
            return False
    return True


def choose_preferences(number_of_couples, solving_method):
    for widgets in f5.winfo_children():
        widgets.destroy()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f5.configure(bg='#FFBBBC')

    home_btn = Button(f5, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.pack(padx=600, pady=50)
    Label(f5, text="Set the preferences using the format: <A,B,C> for men and <1,2,3> for women.", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 14 bold').place(
        x=150, y=100)

    Label(f5, text="Men", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=200, y=150)
    Label(f5, text="Women", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=700, y=150)

    faq_btn = Button(f5, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f5, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)
    entry_array_men = []
    entry_array_women = []

    def create_preferences():
        preferences_men = {}
        preferences_women = {}

        index = 1
        for entry in entry_array_men:
            string_list = entry.get()
            local_pref = string_list.split(',')
            preferences_men[str(index)] = local_pref
            index += 1
        index = 1
        for entry in entry_array_women:
            string_list = entry.get()
            local_pref = string_list.split(',')
            preferences_women[chr(index + 64)] = local_pref
            index += 1

        if input_from_user_is_correct(preferences_men, preferences_women, number_of_couples) is True:
            men_list, women_list = solve_problem(number_of_couples,preferences_men, preferences_women, solving_method)
            show_solution(men_list, number_of_couples, solving_method)
        else:
            Label(f5, text="The input is incorrect!", borderwidth=0, bg="#FFBBBC", fg='#F04755',
                  font='Montserrat 16 bold').place(x=400, y=650)

    y = 200

    for index in range(1, int(number_of_couples) + 1):
        Label(f5, text=index, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=100, y=y)
        entry_man = Entry(f5)
        entry_man.place(x=130, y=y)
        entry_man.config(borderwidth=0, highlightbackground='#F04755', highlightthickness=3, bg="#FFFFFF", fg='#F04755',
                         font='Montserrat 14 bold')
        entry_array_men.append(entry_man)

        Label(f5, text=chr(index + 64), borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(
            x=650, y=y)
        entry_woman = Entry(f5)
        entry_woman.place(x=670, y=y)
        entry_woman.config(borderwidth=0, highlightbackground='#F04755', highlightthickness=3, bg="#FFFFFF",
                           fg='#F04755',
                           font='Montserrat 14 bold')
        entry_array_women.append(entry_woman)
        y = y + 50

    submit_img = PhotoImage(file="submit.png")
    submit_btn = Button(f5, image=submit_img, borderwidth=0, bg="#FFBBBC", command=create_preferences)
    submit_btn.place(x=450, y=670)

    Label(f5, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=450,
                                                                                                              y=730)

    raise_frame(f5)
    root.mainloop()


def random_preferences(number_of_couples, solving_method):
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
    men_list, women_list = solve_problem(number_of_couples,preferences_men, preferences_women, solving_method)
    show_solution(men_list, number_of_couples, solving_method)


def submit_preferences(number_of_couples, solving_method, preferences):
    if preferences == "Manual":
        choose_preferences(number_of_couples, solving_method)
    else:
        random_preferences(number_of_couples, solving_method)


def match():
    print("pressed the match")
    for widgets in f4.winfo_children():
        widgets.destroy()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f4.configure(bg='#FFBBBC')

    Label(f4, text="Number of couples", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').pack(
        side=TOP, anchor=W, padx=300, pady=250)
    Label(f4, text="Solving method", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=300,
                                                                                                                 y=350)
    Label(f4, text="Preferences", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=330,
                                                                                                              y=450)

    couples_variable = StringVar(f4)
    couples_variable.set("1")
    couples = OptionMenu(f4, couples_variable, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    couples.place(x=630, y=250)
    couples.config(borderwidth=0, highlightbackground='#F04755', highlightthickness=3, bg="#FFFFFF", fg='#F04755',
                   font='Montserrat 14 bold')

    solving_method_variable = StringVar(f4)
    solving_method_variable.set("Greedy")
    method = OptionMenu(f4, solving_method_variable, "Greedy", "Backtracking")
    method.place(x=580, y=355)
    method.config(borderwidth=0, highlightbackground='#F04755', highlightthickness=3, bg="#FFFFFF", fg='#F04755',
                  font='Montserrat 14 bold')

    preferences_variable = StringVar(f4)
    preferences_variable.set("Random")
    preferences = OptionMenu(f4, preferences_variable, "Random", "Manual")
    preferences.place(x=565, y=455)
    preferences.config(borderwidth=0, highlightbackground='#F04755', highlightthickness=3, bg="#FFFFFF", fg='#F04755',
                       font='Montserrat 14 bold')

    submit_img = PhotoImage(file="submit.png")
    submit_btn = Button(f4, image=submit_img, borderwidth=0, bg="#FFBBBC",
                        command=lambda: submit_preferences(couples_variable.get(), solving_method_variable.get(),
                                                           preferences_variable.get()))
    submit_btn.place(x=450, y=550)

    Label(f4, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=450,
                                                                                                              y=730)

    home_btn = Button(f4, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.place(x=600, y=50)
    faq_btn = Button(f4, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)

    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f4, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)

    raise_frame(f4)
    root.mainloop()


def faq():
    for widgets in f3.winfo_children():
        widgets.destroy()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f3.configure(bg='#FFBBBC')

    Label(f3, text="Questions and Answers", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').pack(
        side=TOP, anchor=W, padx=100, pady=130)
    Label(f3,
          text=" Q: What is the stable marriage problem? \n A: Ahe stable marriage problem (also stable matching problem "
               "or SMP) is the problem of finding \n a stable matching between two equally sized sets of elements given an"
               " ordering of preferences \n for each element. \n\n Q: What is a Greedy Algorithm? \n A: A greedy algorithm"
               " is any algorithm that follows the problem-solving heuristic of making \n the locally optimal choice at "
               "each stage. In many problems, a greedy strategy does not \n produce an optimal solution, but a greedy "
               "heuristic can yield locally optimal solutions that \n approximate a globally optimal solution in a reasonable "
               "amount of time. \n\n Q: What is Backtracking? \n A: Backtracking is a class of algorithms for finding "
               "solutions to some computational \n problems, notably constraint satisfaction problems, that incrementally "
               "builds candidates to \n the solutions, and abandons a candidate (backtracks) as soon as it determines that"
               " the \n candidate cannot possibly be completed to a valid solution",
          borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 16'), justify=LEFT).place(x=70, y=250)

    home_btn = Button(f3, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.place(x=600, y=50)
    faq_btn = Button(f3, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f3, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)

    raise_frame(f3)
    root.mainloop()


def home():
    for widgets in f1.winfo_children():
        widgets.destroy()
    print("pressed the home")
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


def description_page():
    for widgets in f2.winfo_children():
        widgets.destroy()
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
          borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 20'), justify=LEFT).place(x=40,y=300)
    back_arrow = PhotoImage(file="back_arrow.png")

    back_btn = Button(f2, text="Back", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      image=back_arrow, command=start_app)
    back_btn.place(x=30, y=30)
    raise_frame(f2)
    root.mainloop()


def start_app():
    for frame in (f1, f2, f3, f4, f5, f6):
        frame.grid(row=0, column=0, sticky='news')
    home()


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


def get_rank(list_of_preferences, person):
    return list_of_preferences.index(person)


def greedy_approach(men, women, preferences_men, preferences_women):
    print("GREEDY")
    print(preferences_men)
    print(preferences_women)
    print(men)
    print(women)
    # Storing the number of men and women
    number_of_men = len(men)
    number_of_women = len(women)

    # Keeping a list of unmarried men
    list_of_unmarried_men = men

    # As default, each person is single
    partner_man = {}
    for man in men:
        partner_man[man] = None
    partner_woman = {}
    for woman in women:
        partner_woman[woman] = None

    # Keep the next step of each men
    next_man_choice = {}
    for man in men:
        next_man_choice[man] = 0

    # State is the number of couples, when we have n couples, a list will be returned
    state = 0

    while state < number_of_men:
        # Choose a random man
        random_man = random.choice(list_of_unmarried_men)
        # Take his actual preference
        preference_man = preferences_men[random_man][next_man_choice[random_man]]
        # Check actual woman partner
        actual_partner_woman = partner_woman[preference_man]

        if actual_partner_woman is None:
            # If she is single, we can create a couple
            list_of_unmarried_men.remove(random_man)
            partner_woman[preference_man] = random_man
            partner_man[random_man] = preference_man
            next_man_choice[random_man] += 1

            # Now we have one more couple
            state += 1
        else:
            # She already has a partner
            # Check the rank of his actual partner

            partner_rank = get_rank(preferences_women[preference_man], actual_partner_woman)
            random_man_rank = get_rank(preferences_women[preference_man], random_man)

            if random_man_rank > partner_rank:
                # She gets a new partner
                list_of_unmarried_men.remove(random_man)
                list_of_unmarried_men.append(actual_partner_woman)
                partner_woman[preference_man] = random_man
                partner_man[random_man] = preference_man
                next_man_choice[random_man] += 1
            else:
                next_man_choice[random_man] += 1
    return partner_man, partner_woman


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

'''
-------------------BKT-----------------------
'''

N = 0
states = list()
solutions_bkt = list()
output_solutions = list()
count = 0
counter = 0


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
    if i == N:
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


def create_bkt_preferences(preferences_men,preferences_women):
    males=[]
    women=[]
    for key,values in preferences_men.items():
        women_list=[]
        for value in values:
            woman= ord (value)-65
            women_list.append(woman)
        males.append(women_list)
    for key,values in preferences_women.items():
        men_list=[]
        for value in values:
            if value != '10':
                man= ord (value)-49
                men_list.append(man)
            else:
                man = 10
                men_list.append(man)
        women.append(men_list)
    mp=array(males)
    wp=array(women)
    return mp,wp


def solve_problem(number_of_couples,preferences_men, preferences_women, solving_metho):
    men = create_person_list(preferences_men)
    women = create_person_list(preferences_women)

    if solving_metho == 'Greedy':
        return greedy_approach(men, women, preferences_men, preferences_women)
    else:
        mp,wp = create_bkt_preferences(preferences_men,preferences_women)
        print(mp)
        print(wp)
        solutie1,solutie2 = bkt_approach(int(number_of_couples), mp, wp)
        print(solutie1,solutie2)
        return solutie1,solutie2


if __name__ == '__main__':
    start_app()

