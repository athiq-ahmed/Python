# =============================================================================
# https://www.tutorialspoint.com/python/python_while_loop.htm
# =============================================================================

#while loop - Basic
count = 0;
while (count<9):
    print ("The count is ", count)
    count = count + 1

#while loop - with else condition
count = 0;
while (count<9):
    print ("The count is ", count)
    count = count + 1
else:
    print("The count reached", count)
    

count = 0
while (count < 1):
    print ("Keeps going")
#Ctrl+c to break the run statement
    
#for loop - Basic
for i in range (10):
    print(i)

for i in 'Python':
    print(i)

variables = ['Athiq','Ahmed','Mysore']
for i in variables:
    print(i)

fruits = ['banana','apple','mango']
for i in range(len(fruits)):
    print ("Current fruit is ", fruits[i])

#for loop - with else condition
for i in range(10):
    if i < 5:
        print ("The current number is less than 5,ie ",i)
    else:
        print("The current number is greater then 5,ie ",i)

#Nested loops
for i in range(5,10):
    for j in range(10,15):
        if i + j > 10:
            print (i+j)


count = 0
while (count <9):
    print ("Its running....")
    break

for i in "Python":
    if i == "t":
        break
    else:
        print (i)
    
count = 0
while (count <9):
    print ("Its running....")
    continue

for i in "Python":
    if i == "t":
        continue
    else:
        print (i)


count = 0
while (count <9):
    print ("Its running....")
    pass

for i in "Python":
    if i == "t":
        pass
        print("This is the pass statement")
    else:
        print (i)
