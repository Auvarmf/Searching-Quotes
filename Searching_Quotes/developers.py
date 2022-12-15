# modules
class Admin:
  admCount = 0
  
  def __init__(self, name, npm):
      self.name = name
      self.npm = npm
      Admin.admCount += 1

  def displayCount(self):
      print (Admin.admCount)

  def displayAdmin(self):
      print ("\t",self.name,"-",self.npm)
      
adm1 = Admin("Auvar Mahsa Fahlevi", 2117051027)
adm2 = Admin("Hamzah Hanif", 2117051032)
adm3 = Admin("Roy Rafles Matorang Pasaribu", 2117051058)
print (Admin.admCount)

def pengembang():
  print("")
  print("===================================================")
  print("|--\t\tProgram UAP PI \t\t\t--|")
  print("===================================================")
  print("")
  print("----        Selamat Datang Program Kami       ----")
  adm1.displayAdmin()
  adm2.displayAdmin()
  adm3.displayAdmin()
  print("\t\tTotal Developers : ",Admin.admCount)
  print("==================================================")
