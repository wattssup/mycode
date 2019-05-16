#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n************Details of Interface - ' + i + ' **************')
    try:  #THis is a new line, you also need do indent the code below the line by 4 whitespaces
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:   # this is anew line
        print('Could not collect adapter information') # Print na error message

