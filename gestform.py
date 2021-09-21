resultat = 0
for i in range(-1000, 1000):
    if i%3 == 0 and i%5 == 0:
        print('On affiche GESTFORM car i = ', i, 'et est divisible par 3 et 5')
        resultat += i
    elif i%3 == 0:
        print('On affiche GEST car i = ', i,'et est uniquement divisible par 3')
        resultat += 1
    elif i%5 == 0:
        print('On affiche FORM car i = ', i,'et est uniquement divisible par 5')
        resultat += 1
