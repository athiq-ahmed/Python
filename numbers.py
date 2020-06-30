var1 = 10
var2 = 20

del var1, var2

#Python supports four different numerical types −
#    Integers - They are often called just integers or ints, are positive or negative whole numbers with no decimal point.
#    Long - Also called longs, they are integers of unlimited size, written like integers and followed by an uppercase or lowercase L.
#    Float - Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).
#    complex - are of the form a + bJ, where a and b are floats and J (or j) represents the square root of -1 (which is an imaginary number). 

#int	       long	              float	         complex
#10	       51924361L	        0.0  	          3.14j
#100	      -0x19323L	        15.20	          45.j
#-0x260	  -052318172735L	    -32.54e100	   3e+26J

#Number type conversion
a =10
type(a)

b = float(a)
type(b)

c = complex(a)
type(c)


#Mathematical functions
import math
a = -100.52
b = abs(a)
print ("abs(-45): ", abs(-45))
print ("abs(100.12): ", abs(100.12))
#print ("abs(119L): ", abs(119L))

#ceil - This method returns smallest integer not less than x.
c = math.ceil(a)
print ("math.ceil(-45.17): ", math.ceil(-45.17))
print ("math.ceil(100.12): ", math.ceil(100.12))
print ("math.ceil(100.72): ", math.ceil(100.72))
#print ("math.ceil(119L): ", math.ceil(119L))
print ("math.ceil(math.pi): ", math.ceil(math.pi))

#cmp( x, y ) - This method returns -1 if x < y, returns 0 if x == y and 1 if x > y
def cmp(a,b):
    if a < b:
        return (-1)
    elif (a > b):
        return (1)
    elif (a ==b):
        return 0
        
print ("cmp (10,20) is: ", cmp(10,20))
print ("cmp(80, 100): ", cmp(80, 100))
print ("cmp(180, 100): ", cmp(180, 100))
print ("cmp(-80, 100): ", cmp(-80, 100))
print ("cmp(80, -100): ", cmp(80, -100))

#exp
a= math.exp(10*2)
print ("math.exp(-45.17): ", math.exp(-45.17))
print ("math.exp(100.12): ", math.exp(100.12))
print ("math.exp(100.72): ", math.exp(100.72))
#print ("math.exp(119L): ", math.exp(119L))
print ("math.exp(math.pi): ", math.exp(math.pi))

#fabs - This method returns absolute value of x
a = math.fabs(-10.43)
print ("math.fabs(-45.17): ", math.fabs(-45.17))
print ("math.fabs(100.12): ", math.fabs(100.12))
print ("math.fabs(100.72): ", math.fabs(100.72))
#print ("math.fabs(119L): ", math.fabs(119L))
print ("math.fabs(math.pi): ", math.fabs(math.pi))

#floor - This method returns largest integer not greater than x.
a = math.floor(19.99)
print ("math.floor(-45.17): ", math.floor(-45.17))
print ("math.floor(100.12): ", math.floor(100.12))
print ("math.floor(100.72): ", math.floor(100.72))
#print ("math.floor(119L): ", math.floor(119L))
print ("math.floor(math.pi): ", math.floor(math.pi))

#log - This method returns natural logarithm of x, for x > 0.
a = math.log(10)
#print ("math.log(-45.17): ", math.log(-45.17))
print ("math.log(100.12): ", math.log(100.12))
print ("math.log(100.72): ", math.log(100.72))
#print ("math.log(119L): ", math.log(119L))
print ("math.log(math.pi): ", math.log(math.pi))

#sqrt
a = math.sqrt(10)
#print ("math.sqrt(-45.17): ", math.sqrt(-45.17))
print ("math.sqrt(100.12): ", math.sqrt(100.12))
print ("math.sqrt(100.72): ", math.sqrt(100.72))
#print ("math.sqrt(119L): ", math.sqrt(119L))
print ("math.sqrt(math.pi): ", math.sqrt(math.pi))

#Random number functions
#choice(seq) - The method choice() returns a random item from a list, tuple, or string.
import random
print("choice[1,2,4,5,10]: ",random.choice([1,2,4,5,10]))
print("Python is good: ",random.choice("Python is good"))

#randrange() - The method randrange() returns a randomly selected element from range(start, stop, step).
#randrange ([start,] stop [,step])
print("random.randrange(10,20,1): ",random.randrange(10,20,1))

#random - The method random() returns a random float r, such that 0 is less than or equal to r and r is less than 1.
print("random: ",random.random())

#seed - The method seed() sets the integer starting value used in generating random numbers. Call this function before calling any other random module function.
random.seed(10)
print("",random.random())

#shuffle - This method returns reshuffled list.
list = [1,3,4,6]
random.shuffle(list)
print("random list is: ", list)

#uniform - The method uniform() returns a random float r, such that x is less than or equal to r and r is less than y
print("The random numbers are: ",random.uniform(1,2))


#Trignometric functions
#sin - This method returns a numeric value between -1 and 1, which represents the sine of the parameter x.
print("sin(3) is: ",math.sin(10))

#hypot - The method hypot() return the Euclidean norm, sqrt(x*x + y*y)
print("math.hypot(10,20) is: ",math.hypot(1,2))

#cos - The method cos() returns the cosine of x radians
print("math.cos(10): ",math.cos(10))

#tan - The method tan() returns the tangent of x radians
print("math.tan(10): ",math.tan(10))

#degress - The method degrees() converts angle x from radians to degrees
print("math.degrees(10): ",math.degrees(10))

#radians - The method radians() converts angle x from degrees to radians
print("math.radians(10): ",math.radians(10))



