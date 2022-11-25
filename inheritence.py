class A:  # Parent Class
     def feature1(self):
         print('f1 working')

     def feature2(self):
        print('f2 working')


class B:  # Child class
    def feature3(self):
        print('f3 working')

    def feature4(self):
        print('f4 working')
class C(A, B): # multiple
    def feature1(self):
        print('f1 working')

    def feature5(self):
        print('f5 working')


a1 = A()
b1 = B()
c1 = C()
# a1.feature1()
# a1.feature2()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1.feature1()
