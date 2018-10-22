from rpg import *


hero = {'lvl': 1, 'hp': 10, 'atk': 2, 'def': 1, 'exp': 0}
enemy = {'lvl': 1, 'hp': 10, 'atk': 2, 'def': 1}


if attack_order() == 1:
    attacker = hero
    attacker_name = 'You'
    defender_name = 'Enemy'
    defender = enemy

else:
    attacker = enemy
    attacker_name = 'Enemy'
    defender_name = 'You'
    defender = hero


dmg = attack(attacker, defender)
enemy['hp'] = (enemy['hp'] - dmg)

print('%s attacks %s dealing %d damage.' % (attacker_name, defender_name, dmg))
print(enemy)



