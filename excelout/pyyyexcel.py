#!/usr/bin/env python3

import pyexcel
import datetime as dt

def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_city = input("What City is " + input_driver + " located in? ")
    input_state = input("What state is this device located in? ")
    d = {"IP": input_ip, "driver": input_driver, "City": input_city, "State": input_state}
    return d

mylistdict = []

print("Hello! This program will make you a *.xls file")

while (True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue or 'q' to quit: ")
    if keep_going.lower() == 'q':
        break

today = dt.datetime.now().strftime("%Y-%m-%d")
filename = input("\nWhat is the name of the *.xls file? ")
filename = today + "." + filename + ".xls"  # filename = f"{today}.{filemame}.xls"
pyexcel.save_as(records=mylistdict, dest_file_name=filename)
print(f"The file {filename} should be in your local directory")

