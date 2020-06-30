# =============================================================================
# https://www.tutorialspoint.com/python/python_variable_types.htm
# =============================================================================

# Assiging values to variables
integer_value = 100
float_value =100.0
string_value = 'Athiq'

type(integer_value)
type(float_value)
type(string_value)


# Multiple assignment
a = b = c = 1

type(a)
type(b)
type(c)

a,b,c = 1,2,'Athiq'
type(a)
type(b)
type(c)

# Standard data types
#Python has five standard data types −
    #Numbers
    #String
    #List
    #Tuple
    #Dictionary

#Python Numbers
var1 = 10
var2 = 20

del var1, var2

#Python supports four different numerical types −
    #int (signed integers)
    #long (long integers, they can also be represented in octal and hexadecimal)
    #float (floating point real values)
    #complex (complex numbers)

#int     	    long	             float    	complex
#10	          51924361L	         0.0	       3.14j
#100	      -0x19323L	        15.20	       45.j
#-0x260	   -052318172735L	    -32.54e100	3e+26J


#Python strings
str = 'Hello world'
print (str)
print (str[0:4])
print (str + ' Test')


#Python Lists - A list contains items separated by commas and enclosed within square brackets []
list = ['abcd',786,123411111111111111111111,'john']
tiny_list = [1223, 'aThiq']
new_list = list + tiny_list

#Python Tuples
    #The main differences between lists and tuples are: Lists are enclosed in brackets [ ]
    #and their elements and size can be changed, while tuples are enclosed in parentheses ( )
    #and cannot be updated. 
list = ('abcd',786,123411111111111111111111,'john')
tiny_list = (1223, 'aThiq')
new_list = list + tiny_list

tuple = ('abcd',2.2,'Athiq',123)
list = ['abcd',2.2,'Athiq',123]
tuple[2] = 1000
list[2] = 1000

#Python Dictionary  - It consist of key-value pairs and it sorts the values in ascending by default
#Dictionaries are enclosed by curly braces { } and values can be assigned and accessed using square braces []
dict = {}
dict['one'] = 'This is one'
dict['two'] = 'This is two'

tinydict = {'name' : 'Athiq', 'Department' : 'Analytics'}
tinydict2 = {4,5,6,7,1,2,9,8}

print(type(dict))
print(dict['one'])
print(tinydict2)
print(dict.keys())
print(dict.values())


#Data type conversions
var1 = 10.0
type(var1)

var2 = int(var1)
type(var2)

var3 = float(var2)
type(var3)

var4 = chr(var2)
type(var4)

var5 = {'name':'Athiq','name2':'Ahmed'}
var6 = ('athiq','ahmed','new')
var7 = tuple(var6)

