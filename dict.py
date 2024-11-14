dict = {
    "name" : "john",
    "age" : 25,
    "color" : "white"
}
print(dict) # print whole

print(dict.get("name")) #print specif key

print(dict.keys()) #print only keys in dictionary

print(dict.values()) #print  only values in dictionary

dict["status"] =  "married" #add new key value pair
print(dict)

dict.update ({"origin" : "Japan"})
print(dict)

dict.pop("age")#remove specified item
print(dict)

dict.popitem()#remove last inserted item
print(dict)

del dict["status"]# deletes selected key item
print(dict)

#del dict  #deletes the entire dictionary
print(dict)

#dict.clear() #clears everything
print(dict)


mydict = dict.copy()# making a copy of the dictionary using copy()
print(mydict)


#nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


#membership dictionaries check if keys are present if not it will print false and we use in

car = {'tyres':21, 'body':'wagon','engine':'5.5cc'}

print('tyres' in car) #true

print('lenght'  in car) #false