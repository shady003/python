class A:  # Parent Class
     def __init__(self):
         print('CONSTRUCTOR : A')



     def feature1(self):
         print('f1 working')

     def feature2(self):
        print('f2 working')


class B(A):  # Child class
    def __init__(self):
        super().__init__()
        print('CONSTRUCTOR : B')

    def feature3(self):
        print('f3 working')


a1 = A()
b1 = B()


