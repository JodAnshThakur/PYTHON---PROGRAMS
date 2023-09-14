string_check = "checking all functions in this string."
#Different functions ::
print(string_check.capitalize())
print(string_check.upper())
print(string_check.lower())
print(string_check.isdigit())  #returns true if all the functions in the string are digit
print(string_check.isspace())
print(string_check.isupper())
print(string_check.islower())


from operator import concat

string = "String for slicing"
new_string =concat(string , " to make concept *cc*")
print(new_string)
print(new_string.index('s'))


