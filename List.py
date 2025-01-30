myList=['Ram','16','Rithika','5']
#print(myList) #print entire list
#print(myList[0]) #print first element
#print(myList[1:3]) #print 2nd and 3rd element
#print(myList[2:]) #print 3rd element to end
#print(myList[:3]) #print 1st to 3rd element
#print(myList[:-3]) #print 1st to 3rd element in the reverse order 

myList.append('Java') #add element to the list
myList.remove('16') #remove element from the list
myList.reverse() #reverse the list
myList.sort(reverse=True) #sort the list in reverse order

print(myList) #print entir list

for x in myList:
    print(x) #print each element of the list

for x in enumerate(myList):
    print(x) #print index and element of the list

for index, value in enumerate(myList):
    print(index, value) #print index and element of the list

#tuple
myTuple=('Ram','16','34','5')
print(myTuple) #print entire tuple --- Tuple Cannot be deleted or modified , 

#SIngle element always use comma in Tuple. Normal bracket
myTuple=('Ram',) #single element tuple