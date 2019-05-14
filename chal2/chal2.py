#!/usr/bin/env python3
list1 = []
dict1 = {"first_name": "Monty", "last_name": "Python", "actions": ["Scooter", 2, "Moscow"]}

print (f'In {dict1["first_name"]} {dict1["last_name"]}, Eric Idle rode a {dict1["actions"][0]} {dict1["actions"][1]} {dict1["actions"][2]} ')

list1.append("horse")
list1.extend(["to", "the Holy Grail"])
print(list1)


