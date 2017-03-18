
class A:

    def __init__(self):
        self.name = 'object of class A'
        self.can_run = True
        self.can_jump = False
        self.can_fly = False
    def run(self):
        print('I can run')

    def list_abilities(self):
        print(self.name)
        print('Can run:', self.can_run)
        print('Can jump:', self.can_jump)
        print('Can fly:', self.can_fly)
        print()

class B:

    def __init__(self):
        self.name = 'object of class B'
        self.can_run = False
        self.can_jump = True
        self.can_fly = False

    def run(self):
        print('I can not run')

    def jump(self):
        print('I can jump')

    def list_abilities(self):
        print(self.name)
        print('Can run:', self.can_run)
        print('Can jump:', self.can_jump)
        print('Can fly:', self.can_fly)
        print()


class C(A,B):

    def __init__(self):
        super().__init__()
        self.name = 'object of class C'
        self.can_fly = True

    def fly(self):
        print('I can fly')

    def list_abilities(self):
        print(self.name)
        print('Can run:', self.can_run)
        print('Can jump:', self.can_jump)
        print('Can fly:', self.can_fly)
        print()


a = A()
b = B()
c = C()

# check hierarchy
print(a.name)
a.run()
a.list_abilities()
print(A.__mro__)
print()

print(b.name)
b.jump()
b.run()
print(B.__mro__)
b.list_abilities()
print()

print(c.name)
c.run()
c.jump()
c.fly()
print(C.__mro__)
c.list_abilities()
print()