#!/usr/bin/env python3

import crayons

#print 'red_string' in red
print(crayons.red('red string'))

# Red  White and Blue text
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.disable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.DISABLE_COLOR = False # enable the crayons package

# THis line will print in color
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

#print 'red string' in read
print(crayons.red('red string', bold=True))

#print 'yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

#print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

#print 'white string' in white
print(crayons.white('white string', bold=True))


