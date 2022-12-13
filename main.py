#no duplicates in a given array
 
l1 = eval(input('Enter a list of elements: '))
print(l1)
l2 = [] 

for i in l1: 
    if( i not in l2):
      l2.append(i)

print(l2)


#solution using SET() constructor

l3 = eval(input('Enter a list of elements version 2: '))
noDuplicates = set(l3)
print(noDuplicates)

#*********************************************************** 
print('****************************')

#count vowels of a given string

myInput = (input('Enter a string: '))
print(myInput)
vowelsList = []


for item in myInput:  
    if(item == 'a'):
      vowelsList.append(item) 
    elif(item == 'e'):
      vowelsList.append(item)
    elif(item == 'i'):
      vowelsList.append(item)
    elif(item == 'o'):
      vowelsList.append(item)
    elif(item == 'u'):
      vowelsList.append(item)

print(len(vowelsList))