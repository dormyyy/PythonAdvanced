from abc import ABC, abstractmethod


class C:
    pass


class B(C):
    pass


class A(B, C):
    pass


#порядок будет: А - В - С (с А в В, потом с В в С и поскольку В уже наследует С то к А возвращатся не нужно)
print(A.mro())
