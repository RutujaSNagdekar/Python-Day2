people={'lisa':'yellow','vinod':'purple','jenny':'pink','Arhan':'Blue'}

#number of student in list

print("number 0f students in the list:",len(people))

people.update({'lisa':'red'})

print(people)

del people['jenny']

people = people.items()
#dict_items([('lisa', 'red'), ('vinod', 'purple'), ('Arhan', 'Blue')])

print(people)
#people = list(people) #Makes list of keys only
people = list(people)
print(people)
people.sort()
print("Sorted List",people)
print(dict(people))


