class emp:
  def __init__(self,name,id):
    self.name = name
    self.id = id 

  def show(self):
    print(f"The name of employee is {self.name} and id is {self.id} ")

class programmer(emp):
  def showlan(self):
    print("The default language is python ")



obj = emp("hari",1045)
obj.show()
# obj.showlan() did not get access it 
obj1 = programmer("harry",6433)  # can get access both class 
obj1.showlan()
obj1.show()