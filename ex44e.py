# this is ex44e.py
# pull from repo 20181109
class Parent(object):

    def override(self):
        print("ohter override()")

    def implicit(self):
        print("other implicit()")

    def altered(self):
        print("other altered()")

class Child(object):

    def __init__(self):
        self.other = Parent()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("Child, befoooooore other altered()")
        self.other.altered()
        print("Child, after other altered()")

son = Child()
son.implicit()
son.override()
son.altered()
