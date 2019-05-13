#/usr/bin/env python3

mylist = ["cat", "dog", 7]
print(mylist)
#To print dog
print(mylist[1])
#I have a cat and a dog that are 7
print(f"I have a {mylist[0]} and a {mylist[1]} that are {mylist[2]}.")

print("my {} string".format("first"))

mylist.append("hampster")

print(mylist)

print(mylist.pop())
mylist.insert(1, "squirrel")
print(mylist)



