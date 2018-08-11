string1 = input("Type a string \n")

string2 = ''.join(reversed(string1))
string3 = string1[::-1]

print("You entered: %s" % string1)

print(string2)
print(string3)
print(string1[::-1])