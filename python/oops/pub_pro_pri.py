class animal:
    def __init__(self):
        #self is similar to this in java and c++
        self.public_variable = "iam a public variable"
        self._protected_variable = "iam a protected variable"
        self.__private_variable = "iam a private variable"


class fruit:
    def __init__(this,name,color):
        #self is not a keyword like this, its just a convention.any other word can be used instead of self,but using self is a good practice
        this.name = name
        this.color = color

dog = animal()
#all the attributes in a class in python are PUBLIC
#using _ is just a convention! it conveys not to be accessed but dont restrict the access

print(dog.public_variable)
print(dog._protected_variable)
print(dog._animal__private_variable)#name mangling

orange = fruit("orange","safroon")
print(orange.color)#safroon