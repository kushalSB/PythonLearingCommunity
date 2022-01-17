class Parent:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Child(Parent): #inheritance
  pass

class Child(Parent):
  def __init__(self, fname, lname):
    Parent.__init__(self, fname, lname)



class Child(Parent):
  def __init__(self, fname, lname):
    super().__init__(self, fname, lname)

#Scope 
#private mode , public mode, protected mode
# __iter__ __next__ __main__ __str__

#BST 