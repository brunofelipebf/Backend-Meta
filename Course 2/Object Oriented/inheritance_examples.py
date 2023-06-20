#first class
class first_name:
    name = 'Bruno'

#second class
class last_name:
    surname = 'Sousa'


#class that bundles other classes
class Full_name(first_name, last_name):
    pass


#instance of the object
full_name = Full_name()

print(full_name.name + " " + full_name.surname)