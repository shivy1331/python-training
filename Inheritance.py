class ParentClass:
   pass
class ChildClass(ParentClass):
   pass
class Grandfather:
    def _init_(self):
        self.hobby = "Reading the news"
    def speak(self):
        print("I am Grandfather. Hobby:", self.hobby)

class Father(Grandfather):
    def _init_(self):
        super()._init_()
        self.job = "Engineer"
    def speak(self):
        print("I am Father. Job:", self.job)

class Child(Father):
    def _init_(self):
        super()._init_()
        self.school = "ABC School"
    def speak(self):
        print("I am Child. School:", self.school)

# Create objects and call methods
gf = Grandfather()
gf.speak()

ft = Father()
ft.speak()

ch = Child()
ch.speak()


