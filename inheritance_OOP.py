#=================
#Example 1
#=================

class animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def __str__(self):
        return f'(name: {self.name} age: {self.age})'
    def get_age(self):
        return self.age
    def set_name(self, name = ""): #setter
        self.name = name


def animal_list(list1,list2):
    final_list = []
    for index in range(len(list1)):
        a = animal(list1[index])
        final_list.append(a)
        a.set_name(list2[index])
    return final_list
# l1 = ['bobby','manny','dave']
# l2 = [1,4,7]
# for index in animal_list(l2,l1):
#     print(index)

#NB. when  a list or dictionary contains a class. printing the list/dictionary will only give you memory location of the class in it and not what you set in __str__ to solve this we loop through each item in the list and print it 


#=================
#Inheritance
#=================

#inheritance is a way og giving a class data type the attributes of another data type when a class inherits another it inherits all data attributes and method more data can be added and behaviors and methods can be override 

class cat(animal):
    def pattern(self,pattern = ""):
        print(pattern)

# cats = cat(4)
# cats.pattern('blue')
# print(cats.pat())

class person(animal):
    def __init__(self, age, name):
        animal.__init__(self,age)
        self.set_name(name)
        self.friends = []
p = person(2,'ben')
print(p)


class rabbit(animal):
    id = 1
    def __init__(self, age,p1 = None,p2 = None):
        super().__init__(age)
        self.rid = rabbit.id
        self.p1 = p1
        self.p2 = p2
        rabbit.id += 1
    def rabbit_age(self):
        return self.age

# r1 = rabbit(1)
# print(r1.rid)
# r2 = rabbit(3)
# print(r2.rid)
# r3 = rabbit(9)
# print(r3.rid)
# r4 = rabbit(15)
# print(r4.rid)