def famous_births(figures):

    sorted_figures = sorted(figures.values(), key=lambda person: int(person["date_of_birth"]))

    for person in sorted_figures:
        print(f'{person["name"]} is a gret scientist born in {person["date_of_birth"]}.')

scientists = {
    "a": { "name": "d", "date_of_birth": "1111"},
    "b": { "name": "u", "date_of_birth": "3333"},
    "c": { "name": "m", "date_of_birth": "2000"},
}

famous_births(scientists)