def info():
    print('om het programma te sluiten type quit')
    naam = input('wat is jou naam: ')
    if naam == 'quit':
        quit()
    leeftijd = input('wat is jou leeftijd: ')
    if leeftijd == 'quit':
        quit()
    print('hallo {}'.format(naam) + ' je leeftijd is {}'.format(leeftijd))

while True:
    info()