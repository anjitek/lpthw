# this is ex44.py

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("Parent override()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, beeeeeeeeefore Parent altered()")
        super(Child, self).altered() # this line is important, inherit from parent class
        print("CHILD, A---FTER Parent altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
