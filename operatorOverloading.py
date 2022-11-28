class Student :
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)
        return m3

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m1)

if s1 > s2 :
    print('Win s1')
else:
    print('Win s3')
print(s1)