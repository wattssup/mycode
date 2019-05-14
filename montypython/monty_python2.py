#!/usr/bin/env python3

round = 0

while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The life of _____"')
    answer = input()
    answer = answer.lower()
    if (answer == 'shrubbery'):
            print('You Gave the Super Secret Answer!')
            break

    elif (answer == 'brian'):
        print('Correct!')
        break
    elif(round == 3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')


