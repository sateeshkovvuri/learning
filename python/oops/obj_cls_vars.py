class fruit():
    nutritious = True
    test_obj = None

    def __init__(self,name,water_content,color):
        self.name = name
        self.water_content = water_content
        self.color = color

    def description(self):
        print(f"{self.name} is {self.color} in color,it has {self.water_content} water content")

    @staticmethod
    def eat(**kwargs):
        if(len(kwargs) == 0): return "you can eat fruits regularly"
        
        test = fruit(kwargs["name"],kwargs["water_content"],kwargs["color"])
        print(f"you can eat {test.name} regularly")
        test_obj = test # test_obj is a local variable
        fruit.test_obj = test #this is the class variable,class variables has to be accessed along with their class names or else they will be treated as local variables
        return test

print(fruit.eat(name="mango",water_content="moderate",color="yellow"))
print(fruit.test_obj)

watermelon = fruit("watermelon","high","green")
watermelon.description()
fruit.eat()
if(fruit.nutritious):
    print("you can eat it regularly")
else :
    print("avoid eating it regularly")

