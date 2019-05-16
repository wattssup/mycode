#!/usr/bin/env python3

mylist = ["192.168.0.5", 5060, "UP"]
##1st item in list

print("The first item in the list (IP): " + mylist[0])

##Second item in List
print("The second item in the list (port): " + str(mylist[1]))

##3rd item in list
print("The last item in the list (state): " + mylist[2])

new_list = [5060, "80", 55 , "10.0.0.1", "10.20.30.1","ssh"]

print(f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")


