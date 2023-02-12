#2. 
myList = ['one', 2, 3.5, True, ['1', '2', '3']]

print ("myList length = ", len(myList))

print("\nSecond Element is", myList[2])

#2.1 replace
myList[3] = 4
myList[0] = 1

print ("3rd Element replaced in myList", myList)

#2.2
myList.append(5)
myList.append(6.5)

print ("My new list", myList)

#2.3
myListlength = len(myList)

print("Length of myList is", myListlength)

#2.4
print (myList[4:7])

myList2 = (['1', '2', '3'], 5, 6.5)

#2.5
print (myList2)

#2.6
myList.extend(myList2)

print('Extended myList', myList)

#2.7
simList = ['1', '2', '3', '5', '4']

#2.8
simList.sort(reverse=False)

print (simList)

#2.9

simList2 = simList.copy()
print('Copied List:', simList2)

#2.10 #can't make this happen HEEEELP!
thisSet = {"apple", "banana", "cherry", "pawpaw"}
thisSet.add("orange")
print("thisSet ... ", thisSet)

#Section 3 TUPLEs
tuple1 = (1, 2, 3, 5, 4,) 

#3.1
tuple2 = tuple1 * 3
print("tuple2 times 3 =", tuple2)

#3.2
print("The 12th element is", tuple2[12])

#3.3 
print(sorted(tuple2))

#3.4
