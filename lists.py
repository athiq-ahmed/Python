# =============================================================================
# https://www.tutorialspoint.com/python/python_lists.htm
# =============================================================================
#Python Lists
#The list is a most versatile datatype available in Python which can be written as a list of 
#comma-separated values (items) between square brackets. Important thing about a list is that 
#items in a list need not be of the same type.

#Examples
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list3 = ['a','b',1,2,3,'d']

#Accessing values in lists
print("list1[1]: ",list1[1])
print("list1[2:4]: ",list1[2:4])

#Updating list
list1[2] = 100
print("Updated list1 is: ", list1)

#Delete list elements
del list1[2]
print("Deleting the list items: ",list1)

#Basic list operations
len([1,2,3])            # length
[1,2,3]+[4,5,6]         # Concatenation
['hi']*4                # Repetition
3 in [1,2,3]            # Membership
for x in [1,2,3]:print(x) # Iteration

#Indexing, Slicing and Matrixes
L=['spam','Spam','SPAM!']
L[2]
L[-2]
L[1:]

#Built in list methods
#cmp(list1, list2) - Compares elements of both lists.
list1= [1,2,3]
list2= [4,5,6]
list3= [4,5,6]
print(cmp(list1,list2))
print(cmp(list3,list2))

#len(list)
list1=[1,2,3,4,5,6,7,8,9,10]
print("len(list1)",len(list1))

#max(list)
print("max(list1): ",max(list1))

#min(list)
print("min(list1): ",min(list1))

#Methods with description
#list.append(obj) - Appends object obj to list
alist = ['athiq','ahmed',100,200]
alist.append('new')
print("The appended list is: ",alist)

#list.count(obj) - Returns count of how many times obj occurs in list
alist = ['athiq','ahmed',100,200]
print("The count of the 'athiq' is: ",alist.count('athiq'))

#list.extend(seq) - Appends the contents of seq to list
alist = ['athiq','ahmed',100,200]
alist.extend('new')
print("The extended list is: ",alist)

alist = ['athiq','ahmed',100,200]
blist = ['new','new1']
alist.extend(blist)
print("The extended list is: ",alist)

#list.index(obj) - Returns the lowest index in list that obj appears
alist = ['athiq','ahmed',100,200]
print(alist.index(100))

#list.insert(index, obj) - Inserts object obj into list at offset index
alist = ['athiq','ahmed',100,200]
alist.insert(1,13)
print(alist)

#list.pop(obj=list[-1]) - Removes and returns last object or obj from list
aList = [123, 'xyz', 'zara', 'abc'];
print ("A List : ", aList.pop())
print ("B List : ", aList.pop(2))

#list.remove(obj) - Removes object obj from list
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('xyz');
print ("List : ", aList)
aList.remove('abc');
print ("List : ", aList)

#list.reverse() - Reverses objects of list in place
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print ("List : ", aList)

#list.sort([func]) - Sorts objects of list, use compare func if given
aList = [ 'xyz', 'zara', 'abc', 'xyz'];
aList.sort()
print ("List : ", aList)





