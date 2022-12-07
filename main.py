
#list functions

myList = [10, 20, 'Name', -10, 30.5]
print(myList)

print(myList[3:5])
print(myList*2)

myList.append(400)
print(myList)

myList.remove('Name')
print(myList)

del(myList[0])
print(myList)

print(max(myList))
print(min(myList))

newIndex = len(myList) 
print(newIndex)

myList.insert(newIndex, 'testing')
print(myList)

myList.remove('testing')

myList.sort(reverse=True)
print(myList)

#tuple - IMMUTABLE

tuple = (1, 2, 2, 2, 3, 'xyz')
print(type(tuple))
print(tuple*4)
print(tuple.count(2))
print(tuple.index('xyz'))

#SET data struc - NOT DUPLICATES - unorder - NOT INDEXING

s = {10, 20, 30, 'xyz'}
print(s)

s.update([500, 600])
print(s)

s.remove('xyz')
print(s)

newSetVar = frozenset(s)
print(newSetVar)

#for loop

for item in myList:
    print(item) 
  
#dictionary 
  
range = range(5)  
newId = 0 
myDic = {1: 'Jhon', 2: 'New', 3: 'Test'} 
k = myDic.keys()
v = myDic.values()

for i in k:
  print(i) 

for i in v:
  print(i)


myNewList = ['GT', 'MX', 'CANADA', 'BRASIL']

 






