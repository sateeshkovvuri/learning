class A:
    def test(self):
        print("testing from A")

class B(A):
    pass

class C(A):
    def test(self):
        print("testing from C")


class D(B,C):
    pass


D().test()
