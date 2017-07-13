def declare_winner(fighter1, fighter2, first_attacker):
    first = fighter1 if fighter1.name == first_attacker else fighter2
    second = fighter2 if fighter1.name == first_attacker else fighter1
    n1 = first.health // second.damage_per_attack + (1 if first.health % second.damage_per_attack else 0)
    n2 = second.health // first.damage_per_attack + (1 if second.health % first.damage_per_attack else 0)
    return first.name if n1 >= n2 else second.name
