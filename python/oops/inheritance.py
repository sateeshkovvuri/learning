class parent:
    def __init__(self,code):
        self.code = code
        print("constructor of parent called")

class child1(parent):
    def __init__(self):
        print("constructor of child1 called")

child1() #by default constructor of parent is not called,it should be explicitly mentioned

class child2(parent ):
    def __init__(self):
        print("constructor of child2 called")
        parent.__init__(self,2505)
        print(self.code)
        #in python there are many ways to do a single task
        #why calling the constructor again!?
        parent.__init__(self,25052003)
        print(self.code)
        #instead this can be done
        self._code = 20526
        print(self.code)

child2()