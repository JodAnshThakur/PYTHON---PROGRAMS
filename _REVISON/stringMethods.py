# Strings are immutable

test = "anshthakur"
number = "55" #This is numeric string
print(test.upper())
print(test.capitalize())
print(test.endswith("r"))
print(test.count('a'))
print(test.isalnum()) # combination of numeric alphabet and numebes, returns true if only num or viceversa only return true if cmbination of  alphabet with numeric values
print(number.isnumeric()) # will return true as number is a numberic string but will return false for test.isnumeric as it is  a pure string 
print(test.isnumeric)  