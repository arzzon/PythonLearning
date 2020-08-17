'''
Regex in python
'''
import re

'''
IMPORTANT:
Python offers two different primitive operations based on regular expressions: 
re.match() checks for a match only at the beginning of the string, while re.search() 
checks for a match anywhere in the string (this is what Perl does by default).
'''
# Find a pattern in the string.
txt = "Hi I'm Arbaaz Khan. Random numbers 12 543 89809"
# If match is not found then a None is returned
matchObject = re.search("vhkdhskhaks", txt)
print(matchObject)  # None

# If match is found then a match object is returned
matchObject = re.search("Khan", txt)
print("Match is found, match object returned:", matchObject)

#Match object
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
print("span is used to return the start and end position of the match (start, end): ", matchObject.span())
print("string is used to return the string passed to the function: ", matchObject.string)
print("group is used to return the part of the string where the pattern was found: ", matchObject.group())

print("########################################")
print("Using match function")
if re.match("Hi", txt):
    print("Using match function: pattern 'Hi' Found")  # Found
else:
    print("Not found")
if re.match("Khan", txt):
    print("Using match function: pattern Found")
else:
    print("Using match function: Pattern 'Khan' Not found")  # Not Found

print("########################################")
print("Using findall() function which returns a list of strings containing all matches.")
print(re.findall('\d+', txt))  # ['12', '543', '89809']

print("########################################")
print("Using split() function which returns a list of strings after splitting it at the patterns.")
print(re.split('\.', txt))  # ["Hi I'm Arbaaz Khan", ' Random numbers 12 543 89809']

print("########################################")
print("Using sub(pattern, replace, string) function which returns the string after replacing the "
      "matched pattern with the replace string.")
print(re.sub('\d+', "*", txt))
