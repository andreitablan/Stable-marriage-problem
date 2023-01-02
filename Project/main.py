from tkinter import *
import random
from PIL import Image, ImageTk

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


def show_solution(solution,number_of_couples, solving_method):
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
    title="The solution using "+solving_method+" is:"
    Label(f6, text=title, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=200,y=100)
    y_man= 200
    y_woman = 200
    for man, woman in solution.items():
        man_image = PhotoImage(file="man1.png")
        Label(f6, text=man,borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 15 bold', image=man_image, compound='center').place(x=200, y=y_man)
        y_man = y_man + 50

        Label(f6, text="is married to", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=250,
                                                                                                                  y=y_woman)
        woman = PhotoImage(file="woman1.png")
        Label(f6, text=woman, borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 15 bold',
              image=man_image, compound='center').place(x=500, y=y_woman)
        y_woman = y_woman + 50


    Label(f6, text="Ⓒ UAIC team", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 16 bold').place(x=450,
                                                                                                              y=730)

    raise_frame(f6)
    root.mainloop()


def choose_preferences(number_of_couples, solving_method):
    for widgets in f5.winfo_children():
        widgets.destroy()
    root.geometry("1024x768")
    root.configure(bg='#FFBBBC')
    f5.configure(bg='#FFBBBC')

    home_btn = Button(f5, text="Home", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                      command=home)
    home_btn.pack(padx=600, pady=50)
    Label(f5, text="Set the preferences", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=350,y=100)

    Label(f5, text="Men", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=200,y=150)
    Label(f5, text="Women", borderwidth=0, bg="#FFBBBC", fg='#F04755', font='Montserrat 25 bold').place(x=700,y=150)

    faq_btn = Button(f5, text="FAQ", borderwidth=0, bg="#FFBBBC", fg='#000000', font='Montserrat 14 bold',
                     command=faq)
    faq_btn.place(x=700, y=50)
    match_img = PhotoImage(file="make_a_match_btn.png")
    match_btn = Button(f5, image=match_img, borderwidth=0, bg="#FFBBBC", command=match)
    match_btn.place(x=780, y=40)

    def create_preferences():
        preferences_men={}
        preferences_women={}
        men_list, women_list = solve_problem(preferences_men, preferences_women, solving_method)
        show_solution(men_list, number_of_couples, solving_method)

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
        list_of_men.append(index)
        list_of_women.append(chr(index + 64))
    for man in list_of_men:
        random.shuffle(list_of_women)
        preferences_men[man] = list(list_of_women)
    for woman in list_of_women:
        random.shuffle(list_of_men)
        preferences_women[woman] = list(list_of_men)
    men_list,women_list = solve_problem(preferences_men,preferences_women,solving_method)
    show_solution(men_list,number_of_couples, solving_method)


def submit_preferences(number_of_couples, solving_method, preferences):
    print(number_of_couples)
    print(solving_method)
    print(preferences)
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
          text=" Q: \n A: \n\n Q: \n A: \n\n Q: \n A:",
          borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 20'), justify=LEFT).pack(side=LEFT, anchor=N,
                                                                                                padx=50, pady=0)

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
          borderwidth=0, bg="#FFBBBC", fg='#F04755', font=('Montserrat 20'), justify=LEFT).pack(side=LEFT, anchor=N,
                                                                                                padx=50, pady=0)
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


def solve_problem(preferences_men, preferences_women, solving_metho):
    men = create_person_list(preferences_men)
    women = create_person_list(preferences_women)

    if solving_metho == 'Greedy':
        return greedy_approach(men, women, preferences_men, preferences_women)
    else:
        pass


if __name__ == '__main__':
    start_app()
