import random


def get_rank(list_of_preferences, person):
    return list_of_preferences.index(person)


def greedy_approach(men, women, preferences_men, preferences_women):
    # Storing the number of men and women
    number_of_men = len(men)

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

