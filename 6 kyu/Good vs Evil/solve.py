def goodVsEvil(good, evil):
    good_worth = {
        'Hobbits': 1, 'Men': 2, 'Elves': 3, 'Dwarves': 3, 'Eagles': 4, 'Wizards': 10,
    }
    evil_worth = {
        'Orcs': 1, 'Men': 2, 'Wargs': 2, 'Goblins': 2, 'Uruk Hai': 3, 'Trolls': 5, 'Wizards': 10
    }
    Hobbits, Men, Elves, Dwarves, Eagles, Wizards = map(int, good.split())
    good_points = Hobbits * good_worth['Hobbits'] + Men * good_worth['Men'] + \
                 Elves * good_worth['Elves'] + Dwarves * good_worth['Dwarves'] + \
                 Eagles * good_worth['Eagles'] + Wizards * good_worth['Wizards']

    Orcs, Men, Wargs, Goblins, Uruk_Hai, Trolls, Wizards = map(int, evil.split())
    evil_points = Orcs * evil_worth['Orcs'] + Men * evil_worth['Men'] +\
                  Wargs * evil_worth['Wargs'] + Goblins * evil_worth['Goblins'] + \
                  Uruk_Hai * evil_worth['Uruk Hai'] + Trolls * evil_worth['Trolls'] + \
                  Wizards * evil_worth['Wizards']

    if good_points > evil_points:
        return 'Battle Result: Good triumphs over Evil'
    elif evil_points > good_points:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
