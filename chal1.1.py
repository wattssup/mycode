#!/usr/bin/env python3
a = "Hello"
b = "Sam"
c = "my student number is"
d = "\n******************'"
num = 245

print ("'" + a + " " + b + ", " + c + " " + str(num) + ".\n**********************'")
print ("'", a, b, ",", c, num, end=".\n******************************'\n")
print ("'{} {}, {} {}.\n************************'\n".format(a, b, c, num))
print (f"'{a} {b}, {c} {num}.\n****************'\n")
print (f"'{a} {b}, {c} {num}.", end=f"{d}\n")
