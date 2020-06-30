# =============================================================================
# https://www.tutorialspoint.com/python/python_strings.htm
# =============================================================================

var1 = "Hello world"
var2 = 'hello world'

#Accessing values in strings
print("var1[0:5]: ",var1[0:5])
print("var2[0:5]: ",var1[5:10])

#Updating strings
print("Updated string: ",var1 + ' This is python')

#String special operators
a = 'hello'
b = 'python'

a + b #Concatenation - Adds values on either side of the operator 
a * 2 #Repetition - Creates new strings, concatenating multiple copies of the same string
a[1] #Slice - Gives the character from the given index
a[0:2] #Range Slice - Gives the characters from the given range
'h' in a #Membership - Returns true if a character exists in the given string
'h' not in a #Membership - Returns true if a character does not exist in the given string
print(r'\n') #Raw String - Suppresses actual meaning of Escape characters.
print(R'\n') #Raw String - Suppresses actual meaning of Escape characters.
print('\n') #without 'r' string

#String formatting operator
print('my name is %s and weight is %d' %('Athiq',80))

#Triple quotes
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
print('c:\\nowhere')
print(r'c:\\nowhere')

#Built in string methods
#capitalize() - Capitalizes first letter of string
str='this is string example'
print('this is string example: ',str.capitalize())

#center(width, fillchar) - Returns a space-padded string with the original string centered to a total of width columns
str='this is string example'
print('this is string example: ',str.center(100))

#count(str, beg= 0,end=len(string))- Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
str='this is string example'
print('this is string example: ',str.count('s',0,5))

#find(str, beg=0 end=len(string)) - Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
str='this is string example'
print('this is string example: ',str.find('e'))
print('this is string example: ',str.find('A'))

#index(str, beg=0, end=len(string)) - Same as find(), but raises an exception if str not found.
str='this is string example'
print('this is string example: ',str.index('s'))
print('this is string example: ',str.index('A'))

#isalnum - Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
str='this is string example'
print('this is string example: ',str.isalnum())

str = "this2009";  # No space in this string
print (str.isalnum())

#len - The method len() returns the length of the string
str='this is string example'
print('this is string example: ',len(str))

#lstrip() - Removes all leading whitespace in string.
str='***************this is string example*************'
print('this is string example: ',str.lstrip('*'))
print('this is string example: ',str.rstrip('*'))
print('this is string example: ',str.strip('*'))

#max(str) - Returns the max alphabetical character from the string str.
str='this is string example'
print('this is string example: ',max(str))

#min(str) - Returns the min alphabetical character from the string str.
str='this*is*string*example'
print('this is string example: ',min(str))

#upper() - Converts lowercase letters in string to uppercase.
str='this is string example'
print('this is string example: ',str.upper())




