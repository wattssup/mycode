#!/usr/bin/env python3

## Create a directory
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## Display parts of a dictonary

print(switch['hostname'])
print(switch['ip'])

## Request a 'fake' key
#print(switch['lynx'])

## Request a 'fake' key with .get() method

print("First test - .get()")
print(switch.get('lynx'))

print ("Second test - .get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print("Third test - .get()")
print(switch.get('version'))


print("Forth Test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print ("Sixth test - .pop()")
switch.pop('version') # removes this key and value pair

print(switch.keys()) # Notice the value of version is gone

print(switch.values()) #Notive the value 1.2

print ("Seventh Test - ADD a new value")
switch['adminlogin'] = 'karl08'
print (switch.keys())
print(switch.values())

print ("Eith Test - ADD a new Value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())


