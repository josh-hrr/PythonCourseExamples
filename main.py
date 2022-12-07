
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
  
#range = range(5)  
newId = 0 
myDic = {1: 'Jhon', 2: 'New', 3: 'Test'} 
k = myDic.keys()
v = myDic.values()

for i in k:
  print(i) 

for i in v:
  print(i)

#course challenge

myNewList = ['GT', 'MX', 'CANADA', 'BRASIL'] 
myNewList.append('New') 
print(myNewList) 
popIndex = myNewList.pop(1)
print(popIndex)
print(myNewList) 
myNewList.insert(2, 'Random')
print(myNewList)

b = 5.1//2
print(b)

height = 6.2
heightInMeters = height * 0.0254
print('\ntesting how to separate output')
print(heightInMeters, '\nTesting: ', height)

#formatting float into double
testingFloat = 5.58821
print('%.2f'%(testingFloat))

#sandwich challenge



toppingsList = ['Onions', 'Lettuce', 'Tomato', 'Olives']
chosenList = []

print("Toppings available: ", toppingsList)

myRange = range(3) 
for i in myRange: 
  result = input('Enter topping #' + str(i + 1) + ': ')
  for k in toppingsList:
    if(result == k):
      chosenList.append(result)  

result2 = input('Enter how many you would like: ')
counter = 0  

if(int(result2) > 0):
  counter = int(result2) * 5

print("Toppings enter: ", chosenList, " Note: if you do not see the toppings enter it means you did not choose the ones listed at the beginning therefore they do not exist")
print("Total: ", " $", counter)

