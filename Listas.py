demo_list = [1, 'hello',1.34,True,[1,2,3]] #this contains String, float, boolean and a list
colours = ['red','green','blue','red']

numbers_list = list((1,2,3,4))

print(type(numbers_list))

r = list(range(1,100)) #prints a list of numbers between 1 and 99

print(len(demo_list))#prints the lenght of the list



print(colours[-2])#gives blue as it´s in this reverse position
print(colours[1])#gives green

colours.append('violet')#adds colours to the list
colours.extend(['violet','yellow'])

colours.insert(-1,'violet')#places violet in this reverse position
colours.sort(reverse=True)#sorts out colours in reverse position
print(colours.count('red'))

