def tallena_henkilot(people: tuple):
    with open('henkilot.csv', 'a') as file:
        list = f'{people[0]};{people[1]};{people[2]}\n'
        file.write(list)
        file.close()


tallena_henkilot(('Pekka', 10, 150.5))
