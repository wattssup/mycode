#!/usr/bin/env python3

ipchk = input("Apply and IP Address: ") # this now prompts the user for input

if ipchk == "192.168.70.1": # if a match
    print("Looks like the IP address of the gateway was set: " + ipchk + " This is not recomended.")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else: 
    #If data not provided
    print("You did not provide input.")
