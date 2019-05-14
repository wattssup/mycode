#!/usr/bin/env python3

custlist = []
while(True):
    print('What Channel Do You Want? ')
    custch = int(input ())
    if custch <=0 or custch > 600:
        print("That's not a valid Channel. Please try another channel.")
        continue

    if (custch <= 20):
        print('You should purchase the Basic Package')

    elif (custch <= 50):
        print('You should purchase the Standard Package')

    elif (custch <= 100):
        print('You should purchase the Premium Package')

    elif (custch <= 200):
        print('You should purchase the Premium HD Package')

    elif (custch <=600):
        print('You should purchase the Extras Package')

    else:
        print('Sorry, we do not have that channel')
    custlist.append(custch)
    print('Would you like to price a different channel? Type \'no\' to quit.')
    custans = input()
    custans = custans.lower()
    if (custans == 'no'):
        print('Thanks for Shopping with us today!')
        print(custlist)
        break
