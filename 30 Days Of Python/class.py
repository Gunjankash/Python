class A:
    a=10
    def func(self):
        print(self.a)
class B:
    def func(self):
        print("I am B FUNC")
class C(B,A):
    pass
obj=C()
obj.func()





