from tkinter.scrolledtext import example

my_dict = {"Varya": 2020, "Sergey": 1987, "Dasha": 1957, "Ulya": 2013}
print (my_dict)

my_dict ['Anton']= 1991
print(my_dict)
my_dict.update({"Max": 1873, "Sasha":2002})
del my_dict['Sergey']
print(my_dict)
a= my_dict.pop('Ulya')
print (my_dict.get('Tanya'))
print (a)

my_set = {1,3,2,43.17,7,8,19,15,2,7,10}
print(my_set)
my_set =[1,3,2, 43.17,'hello','aqua']
my_set = set(my_set)
print (my_set)
print (my_set.remove(43.17))
print(my_set)
