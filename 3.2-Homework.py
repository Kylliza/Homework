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
tuple3 = (1, 1, 1, 2) #???

#3.5
a, b, c, d = tuple3 #I don't know what I'm doing...
print(a)
print(b)
print(c)
print(d)

#3.6
tuple4 = (50,) #?
print(tuple4)

#3.7
tuple5 = tuple2 + tuple3
print(tuple5)

#Section 4 Sets
set1 = {1, 2, 3}
#4.1
set1.add("delicious orange") #, "juicy apple", "pear, plain and simple pear"])
set1.add("juicy apple")
print (set1)

#4.2
set1.add("Orange Subaru WRX")
print(set1)

#4.3
oddset = {"Squirtle", "Warturtle", "Blastoise"}

#4.4
set3 = set1.union(oddset)
print(set3)

#4.5
oddset.pop()
print(oddset)

#4.6
set1.clear()
print (set1)

#4.7
oddset.remove("Squirtle")

set3.discard("juicy apple")

#4.8
print(set3)

#Section 5
Pokémon = {'Pokeball':"Squirtle", 'Master Ball': "Mewtwo", '1stGen':1509}

#5.1
Pokémon.get('Pokeball')

#5.2
Pokémon['1stGen'] = "Alexis"
print(Pokémon)

#5.3
Pokémon.update({'Favorite color': 'orange'})
print(Pokémon)

#5.4
Pokémon.update({'List':['rojo', 'amarillo', 'verde']})
print(Pokémon)

#5.5
Pokémon.keys()
print(Pokémon)

#5.6
Pokémon.values()
print(Pokémon)

#5.7

Johto = Pokémon.copy()
print("This is a copy", Johto)

#5.8
Johto.pop('List')
print("This list got POPED!", Johto)

#5.9
Johto.clear()
print("This dictionary got purged :(", Johto)