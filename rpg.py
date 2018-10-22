from random import randrange


def die_roll():
    return randrange(1, 10)


def attack_order():
    h_roll = die_roll()
    e_roll = die_roll()
    if h_roll > e_roll:
        print('Your turn.')
        return 1

    else:
        print('Enemy turn.')
        return 2


def attack(attacker, defender):
    hit = (attacker['atk'] * die_roll()) - (defender['def']) * die_roll()
    if hit > 0:
        return hit

    else:
        return 0


