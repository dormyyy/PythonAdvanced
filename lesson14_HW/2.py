from abc import ABC, abstractmethod


class C:
    #def check(self):
        #print(1)
        #pass
    pass


class B(C):
    def check(self):
        print(1)
        pass
    pass


class A(B, C):
    pass


#порядок будет: А - В - С (с А в В, потом с В в С и поскольку В уже наследует С то к А возвращатся не нужно)
print(A.mro())
c = A()
c.check()
